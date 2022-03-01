# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from email.mime import base
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.clubinfo.views import ClubInfoViewSet
from apps.flowapi.viewsets import FlowTmplViewSet
from apps.recruitmanagement.views import RecruitManagementViewSet
from apps.registrationdata.views import RegistrationDataViewSet


v1_api = DefaultRouter()
v1_api.register("flowtmpl", FlowTmplViewSet, basename="flowtmpl")
v1_api.register("clubinfo", ClubInfoViewSet, basename="clubinfo")
v1_api.register("recruitmanagement", RecruitManagementViewSet, basename="recruitmanagement")
v1_api.register("registrationdata", RegistrationDataViewSet, basename="registrationdata")

url_custom = [
    url("^api/v1/", include(v1_api.urls)),
    # url("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
