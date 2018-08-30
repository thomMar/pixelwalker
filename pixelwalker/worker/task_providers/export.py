# -*- coding: utf8 -*-

from .generic import TaskProvider

import os

class ExportProvider(TaskProvider):
    """This class defines an Export task"""

    def __init__(self, task_id, input_file_path, input_frame_in, input_frame_out, reference_file_path, reference_width, reference_height, split_required):
        """Export initialization

        :param task_id: The task identifier
        :type task_id: int
        :param input_file_path: The input video file path
        :type input_file_path: str
        :param input_frame_in: The first video frame of future exported media
        :type input_frame_in: int
        :param input_frame_out: The last video frame of future exported media
        :type input_frame_out: int
        :param reference_file_path: The reference video file path
        :type reference_file_path: str
        :param reference_width: The reference video width
        :type reference_width: int
        :param reference_height: The reference video height
        :type reference_height: int
        :param split_required: split_export with reference media if True
        :type split_required: bool
        """
        TaskProvider.__init__(self, task_id, input_file_path)
        if os.path.isfile(reference_file_path) is True:
            self.reference_file_path = reference_file_path
            self.reference_file_name = os.path.basename(reference_file_path)
        else:
            self.acknowledge_error()

        self.input_frame_in = str(input_frame_in)
        self.input_frame_out = str(input_frame_out)
        self.split_required = str(split_required)
        self.reference_width = str(reference_width)
        self.reference_height = str(reference_height)


    def execute(self):
        """Using FFmpeg to generate an export"""

        output_directory = os.path.join(os.path.dirname(self.input_file_path), self.input_file_name+"_task-"+str(self.task_id)+"export")
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

         #%05d génère successivement 00001 00002 ....

        if self.split_required == '1':
            self.output_file_path = os.path.join(output_directory, str('SPLIT_'+os.path.splitext(os.path.basename(self.input_file_path))[0]+'.mp4')) #mp4 header only
            command = ['ffmpeg',
                    '-i', self.reference_file_path,
                    '-i', self.input_file_path,
                    '-an',
                    '-filter_complex', '[0]crop=iw/2:ih:0:0,pad=iw*2:ih[left];[1]scale='+self.reference_width+':'+self.reference_height+'[scaled];[scaled]crop=iw/2:ih:iw/2:0[right];[left][right]overlay=w[main],[main]select=between(n\,'+self.input_frame_in+'\,'+self.input_frame_out+'),setpts=PTS-STARTPTS,drawtext=text=''reference'': fontcolor=white: fontsize=24 :box=1: boxcolor=black@0.5 :boxborderw=5:x=(w-text_w)/4.5:y=(h-text_h)/1.1,drawtext=text=''encoded'': fontcolor=white: fontsize=24 :box=1: boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/1.4:y=(h-text_h)/1.1',
                    '-c:v', 'h264',
                    '-b:v', '50M',
                    #'-c:v', 'rawvideo', #format raw tous les piels sont codés
                    #'-pix_fmt', 'yuv420p'
                     self.output_file_path]

        else:
            self.output_file_path = os.path.join(output_directory, str('EXPORT_'+os.path.basename(self.input_file_path)))
            command = ['ffmpeg',
                    '-i', self.input_file_path,
                    '-an',
                    '-vf', 'select=between(n\,'+self.input_frame_in+'\,'+self.input_frame_out+'),setpts=PTS-STARTPTS',
                     self.output_file_path]

        TaskProvider.execute(self, command)

        if os.path.isfile(self.output_file_path) is True:
            data = {}
            data['outputs'] = []
            output = {}
            output['name'] = 'Export'
            output['file_path'] = self.output_file_path
            output['average'] = None
            output['type'] = 'MEDIA'
            data['outputs'].append(output)
            self.acknowledge_success(data)
        else:
            self.acknowledge_error()
