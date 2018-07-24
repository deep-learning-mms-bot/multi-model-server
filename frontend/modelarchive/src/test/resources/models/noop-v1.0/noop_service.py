# Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#     http://www.apache.org/licenses/LICENSE-2.0
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
NoopService defines a noop service
"""

from mms.model_service.mxnet_model_service import SingleNodeService

class NoopService(SingleNodeService):
    """
    NoopService defines a noop service.
    """

    def _inference(self, data):
        return data[0]

    def ping(self):
        return None

    @property
    def signature(self):
        return None