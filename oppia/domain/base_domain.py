# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base domain object."""

__author__ = 'Sean Lip'


class BaseDomainObject(object):
    """Base domain object class for Oppia.

    Domain objects capture domain-specific logic and are agnostic of how the
    objects they represent are stored. All methods and properties in domain
    files should therefore be independent of the specific storage models used.
    """

    class ObjectValidationError(Exception):
        """Error class for domain object validation errors."""