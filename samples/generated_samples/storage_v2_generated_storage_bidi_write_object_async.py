# -*- coding: utf-8 -*-
# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for BidiWriteObject
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-storage


# [START storage_v2_generated_Storage_BidiWriteObject_async]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from google.cloud import storage_v2


async def sample_bidi_write_object():
    # Create a client
    client = storage_v2.StorageAsyncClient()

    # Initialize request argument(s)
    request = storage_v2.BidiWriteObjectRequest(
        upload_id="upload_id_value",
        write_offset=1297,
    )

    # This method expects an iterator which contains
    # 'storage_v2.BidiWriteObjectRequest' objects
    # Here we create a generator that yields a single `request` for
    # demonstrative purposes.
    requests = [request]

    def request_generator():
        for request in requests:
            yield request

    # Make the request
    stream = await client.bidi_write_object(requests=request_generator())

    # Handle the response
    async for response in stream:
        print(response)

# [END storage_v2_generated_Storage_BidiWriteObject_async]
