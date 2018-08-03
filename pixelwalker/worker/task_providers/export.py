# -*- coding: utf8 -*-

from .generic import TaskProvider

import os

class ExportProvider(TaskProvider):
    """This class defines an Export task"""

    def __init__(self, task_id, input_file_path, input_frame_in, input_frame_out, reference_file_path, reference_width, reference_height):
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
        """
        TaskProvider.__init__(self, task_id, input_file_path)
        if os.path.isfile(reference_file_path) is True:
            self.reference_file_path = reference_file_path
            self.reference_file_name = os.path.basename(reference_file_path)
        else:
            self.acknowledge_error()

        self.input_frame_in = str(input_frame_in)
        self.input_frame_out = str(input_frame_out)


    def execute(self):
        """Using FFmpeg to generate an export"""

        output_directory = os.path.join(os.path.dirname(self.input_file_path), self.input_file_name+"_task-"+str(self.task_id)+"export")
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        self.output_file_path = os.path.join(output_directory, str(os.path.basename(self.input_file_path))) #%05d génère successivement 00001 00002 ....
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
