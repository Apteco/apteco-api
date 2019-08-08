# coding: utf-8

# flake8: noqa

"""
    Apteco API

    An API to allow access to Apteco Marketing Suite resources  # noqa: E501

    The version of the OpenAPI document: v2
    Contact: support@apteco.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "0.1.6"

# import apis into sdk package
from apteco_api.api.about_api import AboutApi
from apteco_api.api.audience_compositions_api import AudienceCompositionsApi
from apteco_api.api.audience_hits_api import AudienceHitsApi
from apteco_api.api.audiences_api import AudiencesApi
from apteco_api.api.collection_hits_api import CollectionHitsApi
from apteco_api.api.collections_api import CollectionsApi
from apteco_api.api.cubes_api import CubesApi
from apteco_api.api.directories_api import DirectoriesApi
from apteco_api.api.exports_api import ExportsApi
from apteco_api.api.fast_stats_jobs_api import FastStatsJobsApi
from apteco_api.api.fast_stats_systems_api import FastStatsSystemsApi
from apteco_api.api.files_api import FilesApi
from apteco_api.api.people_stage_api import PeopleStageApi
from apteco_api.api.queries_api import QueriesApi
from apteco_api.api.sessions_api import SessionsApi
from apteco_api.api.shares_api import SharesApi
from apteco_api.api.static_resources_api import StaticResourcesApi
from apteco_api.api.temporary_files_api import TemporaryFilesApi
from apteco_api.api.user_registration_requests_api import UserRegistrationRequestsApi
from apteco_api.api.user_reset_password_requests_api import UserResetPasswordRequestsApi
from apteco_api.api.users_api import UsersApi
from apteco_api.api.visualisations_api import VisualisationsApi

# import ApiClient
from apteco_api.api_client import ApiClient
from apteco_api.configuration import Configuration
from apteco_api.exceptions import OpenApiException
from apteco_api.exceptions import ApiTypeError
from apteco_api.exceptions import ApiValueError
from apteco_api.exceptions import ApiKeyError
from apteco_api.exceptions import ApiException
# import models into sdk package
from apteco_api.models.abstract_render_spec import AbstractRenderSpec
from apteco_api.models.age_rule import AgeRule
from apteco_api.models.audience_calculate_job_detail import AudienceCalculateJobDetail
from apteco_api.models.audience_check_detail import AudienceCheckDetail
from apteco_api.models.audience_check_job_detail import AudienceCheckJobDetail
from apteco_api.models.audience_detail import AudienceDetail
from apteco_api.models.audience_export_detail import AudienceExportDetail
from apteco_api.models.audience_export_job_detail import AudienceExportJobDetail
from apteco_api.models.audience_hit_detail import AudienceHitDetail
from apteco_api.models.audience_hit_summary import AudienceHitSummary
from apteco_api.models.audience_query_result import AudienceQueryResult
from apteco_api.models.audience_result_detail import AudienceResultDetail
from apteco_api.models.audience_result_summary import AudienceResultSummary
from apteco_api.models.audience_summary import AudienceSummary
from apteco_api.models.audience_update_detail import AudienceUpdateDetail
from apteco_api.models.audience_update_summary import AudienceUpdateSummary
from apteco_api.models.calculate_audience_details import CalculateAudienceDetails
from apteco_api.models.capabilities import Capabilities
from apteco_api.models.change_password_details import ChangePasswordDetails
from apteco_api.models.channel_detail import ChannelDetail
from apteco_api.models.channel_statistics import ChannelStatistics
from apteco_api.models.channel_summary import ChannelSummary
from apteco_api.models.check_audience_details import CheckAudienceDetails
from apteco_api.models.check_composition_definition import CheckCompositionDefinition
from apteco_api.models.check_dimension_result import CheckDimensionResult
from apteco_api.models.clause import Clause
from apteco_api.models.collection_detail import CollectionDetail
from apteco_api.models.collection_hit_detail import CollectionHitDetail
from apteco_api.models.collection_hit_summary import CollectionHitSummary
from apteco_api.models.collection_part_detail import CollectionPartDetail
from apteco_api.models.collection_part_summary import CollectionPartSummary
from apteco_api.models.collection_summary import CollectionSummary
from apteco_api.models.column import Column
from apteco_api.models.communication_statistics import CommunicationStatistics
from apteco_api.models.composition_detail import CompositionDetail
from apteco_api.models.composition_summary import CompositionSummary
from apteco_api.models.confirm_reset_password_request import ConfirmResetPasswordRequest
from apteco_api.models.count import Count
from apteco_api.models.create_audience_composition_detail import CreateAudienceCompositionDetail
from apteco_api.models.create_audience_detail import CreateAudienceDetail
from apteco_api.models.create_audience_hit_details import CreateAudienceHitDetails
from apteco_api.models.create_audience_update import CreateAudienceUpdate
from apteco_api.models.create_collection_hit_details import CreateCollectionHitDetails
from apteco_api.models.create_reset_password_request import CreateResetPasswordRequest
from apteco_api.models.create_session_parameters import CreateSessionParameters
from apteco_api.models.create_share_detail import CreateShareDetail
from apteco_api.models.create_share_update import CreateShareUpdate
from apteco_api.models.create_user_registration_request import CreateUserRegistrationRequest
from apteco_api.models.created_share_update_detail import CreatedShareUpdateDetail
from apteco_api.models.criteria import Criteria
from apteco_api.models.cube import Cube
from apteco_api.models.cube_result import CubeResult
from apteco_api.models.dashboard_item import DashboardItem
from apteco_api.models.data_view_details import DataViewDetails
from apteco_api.models.data_view_summary import DataViewSummary
from apteco_api.models.date_rule import DateRule
from apteco_api.models.diagram_metadata import DiagramMetadata
from apteco_api.models.dimension import Dimension
from apteco_api.models.dimension_banding import DimensionBanding
from apteco_api.models.dimension_result import DimensionResult
from apteco_api.models.element_detail import ElementDetail
from apteco_api.models.element_status import ElementStatus
from apteco_api.models.element_summary import ElementSummary
from apteco_api.models.email_requirements import EmailRequirements
from apteco_api.models.endpoint_details import EndpointDetails
from apteco_api.models.error_message import ErrorMessage
from apteco_api.models.error_message_parameter import ErrorMessageParameter
from apteco_api.models.export import Export
from apteco_api.models.export_audience_details import ExportAudienceDetails
from apteco_api.models.export_composition_definition import ExportCompositionDefinition
from apteco_api.models.export_result import ExportResult
from apteco_api.models.expression import Expression
from apteco_api.models.fast_stats_system_detail import FastStatsSystemDetail
from apteco_api.models.fast_stats_system_item import FastStatsSystemItem
from apteco_api.models.fast_stats_system_summary import FastStatsSystemSummary
from apteco_api.models.file_entry import FileEntry
from apteco_api.models.file_stream import FileStream
from apteco_api.models.file_system_summary import FileSystemSummary
from apteco_api.models.folder import Folder
from apteco_api.models.folder_structure_node import FolderStructureNode
from apteco_api.models.fraction import Fraction
from apteco_api.models.grid_item import GridItem
from apteco_api.models.invalid_to_share_user_display_details import InvalidToShareUserDisplayDetails
from apteco_api.models.job_detail import JobDetail
from apteco_api.models.job_summary import JobSummary
from apteco_api.models.language_details import LanguageDetails
from apteco_api.models.last_run_details import LastRunDetails
from apteco_api.models.licence import Licence
from apteco_api.models.limits import Limits
from apteco_api.models.link import Link
from apteco_api.models.list_rule import ListRule
from apteco_api.models.logic import Logic
from apteco_api.models.measure import Measure
from apteco_api.models.measure_result import MeasureResult
from apteco_api.models.message import Message
from apteco_api.models.model_property import ModelProperty
from apteco_api.models.modify_items_modify_user_audience import ModifyItemsModifyUserAudience
from apteco_api.models.modify_items_modify_user_collection import ModifyItemsModifyUserCollection
from apteco_api.models.modify_user_audience import ModifyUserAudience
from apteco_api.models.modify_user_audience_detail import ModifyUserAudienceDetail
from apteco_api.models.modify_user_audience_detail_results import ModifyUserAudienceDetailResults
from apteco_api.models.modify_user_collection import ModifyUserCollection
from apteco_api.models.modify_user_collection_detail import ModifyUserCollectionDetail
from apteco_api.models.modify_user_collection_detail_results import ModifyUserCollectionDetailResults
from apteco_api.models.n_per import NPer
from apteco_api.models.numeric_variable_info import NumericVariableInfo
from apteco_api.models.operation import Operation
from apteco_api.models.output import Output
from apteco_api.models.paged_results_audience_hit_summary import PagedResultsAudienceHitSummary
from apteco_api.models.paged_results_audience_result_summary import PagedResultsAudienceResultSummary
from apteco_api.models.paged_results_audience_summary import PagedResultsAudienceSummary
from apteco_api.models.paged_results_audience_update_summary import PagedResultsAudienceUpdateSummary
from apteco_api.models.paged_results_channel_summary import PagedResultsChannelSummary
from apteco_api.models.paged_results_collection_hit_summary import PagedResultsCollectionHitSummary
from apteco_api.models.paged_results_collection_part_summary import PagedResultsCollectionPartSummary
from apteco_api.models.paged_results_collection_summary import PagedResultsCollectionSummary
from apteco_api.models.paged_results_composition_summary import PagedResultsCompositionSummary
from apteco_api.models.paged_results_data_view_summary import PagedResultsDataViewSummary
from apteco_api.models.paged_results_element_status import PagedResultsElementStatus
from apteco_api.models.paged_results_element_summary import PagedResultsElementSummary
from apteco_api.models.paged_results_endpoint_details import PagedResultsEndpointDetails
from apteco_api.models.paged_results_fast_stats_system_detail import PagedResultsFastStatsSystemDetail
from apteco_api.models.paged_results_fast_stats_system_item import PagedResultsFastStatsSystemItem
from apteco_api.models.paged_results_fast_stats_system_summary import PagedResultsFastStatsSystemSummary
from apteco_api.models.paged_results_file_entry import PagedResultsFileEntry
from apteco_api.models.paged_results_file_system_summary import PagedResultsFileSystemSummary
from apteco_api.models.paged_results_folder_structure_node import PagedResultsFolderStructureNode
from apteco_api.models.paged_results_job_summary import PagedResultsJobSummary
from apteco_api.models.paged_results_modify_user_audience_detail_results import PagedResultsModifyUserAudienceDetailResults
from apteco_api.models.paged_results_modify_user_collection_detail_results import PagedResultsModifyUserCollectionDetailResults
from apteco_api.models.paged_results_people_stage_system_summary import PagedResultsPeopleStageSystemSummary
from apteco_api.models.paged_results_resource_category_summary import PagedResultsResourceCategorySummary
from apteco_api.models.paged_results_resource_summary import PagedResultsResourceSummary
from apteco_api.models.paged_results_session_and_user_details import PagedResultsSessionAndUserDetails
from apteco_api.models.paged_results_share_summary import PagedResultsShareSummary
from apteco_api.models.paged_results_share_update import PagedResultsShareUpdate
from apteco_api.models.paged_results_table import PagedResultsTable
from apteco_api.models.paged_results_user_audience_summary import PagedResultsUserAudienceSummary
from apteco_api.models.paged_results_user_collection_summary import PagedResultsUserCollectionSummary
from apteco_api.models.paged_results_user_display_details import PagedResultsUserDisplayDetails
from apteco_api.models.paged_results_user_registration_request_summary import PagedResultsUserRegistrationRequestSummary
from apteco_api.models.paged_results_user_summary import PagedResultsUserSummary
from apteco_api.models.paged_results_var_code import PagedResultsVarCode
from apteco_api.models.paged_results_variable import PagedResultsVariable
from apteco_api.models.password_requirements import PasswordRequirements
from apteco_api.models.people_stage_system_detail import PeopleStageSystemDetail
from apteco_api.models.people_stage_system_summary import PeopleStageSystemSummary
from apteco_api.models.per_channel_statistics import PerChannelStatistics
from apteco_api.models.per_response_type_per_channel_statistics import PerResponseTypePerChannelStatistics
from apteco_api.models.per_response_type_statistics import PerResponseTypeStatistics
from apteco_api.models.process_details import ProcessDetails
from apteco_api.models.processing_time_statistics import ProcessingTimeStatistics
from apteco_api.models.processing_time_statistics_details import ProcessingTimeStatisticsDetails
from apteco_api.models.query import Query
from apteco_api.models.query_detail_count import QueryDetailCount
from apteco_api.models.query_details import QueryDetails
from apteco_api.models.query_file import QueryFile
from apteco_api.models.query_result import QueryResult
from apteco_api.models.rfv import RFV
from apteco_api.models.rfv_frequency import RFVFrequency
from apteco_api.models.rfv_recency import RFVRecency
from apteco_api.models.rfv_value import RFVValue
from apteco_api.models.range_statistics import RangeStatistics
from apteco_api.models.record_set import RecordSet
from apteco_api.models.render_data_refresh_job_detail import RenderDataRefreshJobDetail
from apteco_api.models.reset_password_request_detail import ResetPasswordRequestDetail
from apteco_api.models.resource_category_details import ResourceCategoryDetails
from apteco_api.models.resource_category_summary import ResourceCategorySummary
from apteco_api.models.resource_details import ResourceDetails
from apteco_api.models.resource_summary import ResourceSummary
from apteco_api.models.response_statistics import ResponseStatistics
from apteco_api.models.response_statistics_per_response_type_statistics_map import ResponseStatisticsPerResponseTypeStatisticsMap
from apteco_api.models.row import Row
from apteco_api.models.rule import Rule
from apteco_api.models.safe_file_handle import SafeFileHandle
from apteco_api.models.selection import Selection
from apteco_api.models.selection_modifiers import SelectionModifiers
from apteco_api.models.selector_variable_info import SelectorVariableInfo
from apteco_api.models.server_message import ServerMessage
from apteco_api.models.session_and_user_details import SessionAndUserDetails
from apteco_api.models.session_details import SessionDetails
from apteco_api.models.share_detail import ShareDetail
from apteco_api.models.share_summary import ShareSummary
from apteco_api.models.share_update import ShareUpdate
from apteco_api.models.size import Size
from apteco_api.models.sub_selection import SubSelection
from apteco_api.models.system_lookup import SystemLookup
from apteco_api.models.table import Table
from apteco_api.models.table_item import TableItem
from apteco_api.models.temporary_file import TemporaryFile
from apteco_api.models.temporary_file_part import TemporaryFilePart
from apteco_api.models.text_variable_info import TextVariableInfo
from apteco_api.models.time_rule import TimeRule
from apteco_api.models.top_n import TopN
from apteco_api.models.transfer_audience_ownership_details import TransferAudienceOwnershipDetails
from apteco_api.models.transfer_collection_ownership_details import TransferCollectionOwnershipDetails
from apteco_api.models.update_user_details import UpdateUserDetails
from apteco_api.models.upsert_collection_detail import UpsertCollectionDetail
from apteco_api.models.upsert_user_collection_detail import UpsertUserCollectionDetail
from apteco_api.models.user_audience_detail import UserAudienceDetail
from apteco_api.models.user_audience_summary import UserAudienceSummary
from apteco_api.models.user_collection_detail import UserCollectionDetail
from apteco_api.models.user_collection_summary import UserCollectionSummary
from apteco_api.models.user_configuration_details import UserConfigurationDetails
from apteco_api.models.user_detail import UserDetail
from apteco_api.models.user_display_details import UserDisplayDetails
from apteco_api.models.user_registration_request_detail import UserRegistrationRequestDetail
from apteco_api.models.user_registration_request_summary import UserRegistrationRequestSummary
from apteco_api.models.user_summary import UserSummary
from apteco_api.models.value_rule import ValueRule
from apteco_api.models.var_code import VarCode
from apteco_api.models.variable import Variable
from apteco_api.models.variable_lookup import VariableLookup
from apteco_api.models.version_details import VersionDetails
from apteco_api.models.visualisation_detail import VisualisationDetail

