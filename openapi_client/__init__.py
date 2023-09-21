# coding: utf-8

# flake8: noqa

"""
    Geo Engine Pro API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.7.0
    Contact: dev@geoengine.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.datasets_api import DatasetsApi
from openapi_client.api.general_api import GeneralApi
from openapi_client.api.layers_api import LayersApi
from openapi_client.api.ogcwcs_api import OGCWCSApi
from openapi_client.api.ogcwfs_api import OGCWFSApi
from openapi_client.api.ogcwms_api import OGCWMSApi
from openapi_client.api.permissions_api import PermissionsApi
from openapi_client.api.plots_api import PlotsApi
from openapi_client.api.projects_api import ProjectsApi
from openapi_client.api.session_api import SessionApi
from openapi_client.api.spatial_references_api import SpatialReferencesApi
from openapi_client.api.tasks_api import TasksApi
from openapi_client.api.uploads_api import UploadsApi
from openapi_client.api.user_api import UserApi
from openapi_client.api.workflows_api import WorkflowsApi

# import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiAttributeError
from openapi_client.exceptions import ApiException

# import models into sdk package
from openapi_client.models.aborted_task_status import AbortedTaskStatus
from openapi_client.models.add_collection200_response import AddCollection200Response
from openapi_client.models.add_dataset import AddDataset
from openapi_client.models.add_layer import AddLayer
from openapi_client.models.add_layer_collection import AddLayerCollection
from openapi_client.models.add_role import AddRole
from openapi_client.models.auto_create_dataset import AutoCreateDataset
from openapi_client.models.auto_ogr_source_time_format import AutoOgrSourceTimeFormat
from openapi_client.models.axis_order import AxisOrder
from openapi_client.models.bounding_box2_d import BoundingBox2D
from openapi_client.models.breakpoint import Breakpoint
from openapi_client.models.classification_measurement import ClassificationMeasurement
from openapi_client.models.classification_measurement_with_type import ClassificationMeasurementWithType
from openapi_client.models.collection_item import CollectionItem
from openapi_client.models.collection_type import CollectionType
from openapi_client.models.color_param import ColorParam
from openapi_client.models.colorizer import Colorizer
from openapi_client.models.completed_task_status import CompletedTaskStatus
from openapi_client.models.continuous_measurement import ContinuousMeasurement
from openapi_client.models.continuous_measurement_with_type import ContinuousMeasurementWithType
from openapi_client.models.coordinate2_d import Coordinate2D
from openapi_client.models.create_dataset import CreateDataset
from openapi_client.models.create_dataset_handler200_response import CreateDatasetHandler200Response
from openapi_client.models.create_project import CreateProject
from openapi_client.models.csv_header import CsvHeader
from openapi_client.models.custom_ogr_source_time_format import CustomOgrSourceTimeFormat
from openapi_client.models.data_id import DataId
from openapi_client.models.data_path import DataPath
from openapi_client.models.data_path_one_of import DataPathOneOf
from openapi_client.models.data_path_one_of1 import DataPathOneOf1
from openapi_client.models.dataset import Dataset
from openapi_client.models.dataset_definition import DatasetDefinition
from openapi_client.models.dataset_id_resource_id import DatasetIdResourceId
from openapi_client.models.dataset_listing import DatasetListing
from openapi_client.models.dataset_resource import DatasetResource
from openapi_client.models.date_time import DateTime
from openapi_client.models.date_time_parse_format import DateTimeParseFormat
from openapi_client.models.default_colors import DefaultColors
from openapi_client.models.default_colors_one_of import DefaultColorsOneOf
from openapi_client.models.derived_color import DerivedColor
from openapi_client.models.derived_color_with_type import DerivedColorWithType
from openapi_client.models.derived_number import DerivedNumber
from openapi_client.models.derived_number_with_type import DerivedNumberWithType
from openapi_client.models.describe_coverage_request import DescribeCoverageRequest
from openapi_client.models.error_response import ErrorResponse
from openapi_client.models.external_data_id import ExternalDataId
from openapi_client.models.external_data_id_with_type import ExternalDataIdWithType
from openapi_client.models.failed_task_status import FailedTaskStatus
from openapi_client.models.feature import Feature
from openapi_client.models.feature_data_type import FeatureDataType
from openapi_client.models.feature_type import FeatureType
from openapi_client.models.file_not_found_handling import FileNotFoundHandling
from openapi_client.models.format_specifics import FormatSpecifics
from openapi_client.models.format_specifics_one_of import FormatSpecificsOneOf
from openapi_client.models.format_specifics_one_of_csv import FormatSpecificsOneOfCsv
from openapi_client.models.gdal_dataset_geo_transform import GdalDatasetGeoTransform
from openapi_client.models.gdal_dataset_parameters import GdalDatasetParameters
from openapi_client.models.gdal_loading_info_temporal_slice import GdalLoadingInfoTemporalSlice
from openapi_client.models.gdal_meta_data_list import GdalMetaDataList
from openapi_client.models.gdal_meta_data_list_with_type import GdalMetaDataListWithType
from openapi_client.models.gdal_meta_data_regular import GdalMetaDataRegular
from openapi_client.models.gdal_meta_data_regular_with_type import GdalMetaDataRegularWithType
from openapi_client.models.gdal_meta_data_static import GdalMetaDataStatic
from openapi_client.models.gdal_meta_data_static_with_type import GdalMetaDataStaticWithType
from openapi_client.models.gdal_metadata_mapping import GdalMetadataMapping
from openapi_client.models.gdal_metadata_net_cdf_cf import GdalMetadataNetCdfCf
from openapi_client.models.gdal_metadata_net_cdf_cf_with_type import GdalMetadataNetCdfCfWithType
from openapi_client.models.gdal_source_time_placeholder import GdalSourceTimePlaceholder
from openapi_client.models.geo_json import GeoJson
from openapi_client.models.get_capabilities_format import GetCapabilitiesFormat
from openapi_client.models.get_capabilities_request import GetCapabilitiesRequest
from openapi_client.models.get_coverage_format import GetCoverageFormat
from openapi_client.models.get_coverage_request import GetCoverageRequest
from openapi_client.models.get_feature_request import GetFeatureRequest
from openapi_client.models.get_legend_graphic_request import GetLegendGraphicRequest
from openapi_client.models.get_map_exception_format import GetMapExceptionFormat
from openapi_client.models.get_map_format import GetMapFormat
from openapi_client.models.get_map_request import GetMapRequest
from openapi_client.models.infinite_ogr_source_duration_spec import InfiniteOgrSourceDurationSpec
from openapi_client.models.internal_data_id import InternalDataId
from openapi_client.models.layer import Layer
from openapi_client.models.layer_collection import LayerCollection
from openapi_client.models.layer_collection_listing import LayerCollectionListing
from openapi_client.models.layer_collection_listing_with_type import LayerCollectionListingWithType
from openapi_client.models.layer_collection_resource import LayerCollectionResource
from openapi_client.models.layer_collection_resource_id import LayerCollectionResourceId
from openapi_client.models.layer_listing import LayerListing
from openapi_client.models.layer_listing_with_type import LayerListingWithType
from openapi_client.models.layer_resource import LayerResource
from openapi_client.models.layer_resource_id import LayerResourceId
from openapi_client.models.layer_update import LayerUpdate
from openapi_client.models.layer_visibility import LayerVisibility
from openapi_client.models.line_symbology import LineSymbology
from openapi_client.models.line_symbology_with_type import LineSymbologyWithType
from openapi_client.models.linear_gradient import LinearGradient
from openapi_client.models.linear_gradient_with_type import LinearGradientWithType
from openapi_client.models.logarithmic_gradient import LogarithmicGradient
from openapi_client.models.logarithmic_gradient_with_type import LogarithmicGradientWithType
from openapi_client.models.measurement import Measurement
from openapi_client.models.meta_data_definition import MetaDataDefinition
from openapi_client.models.meta_data_suggestion import MetaDataSuggestion
from openapi_client.models.mock_dataset_data_source_loading_info import MockDatasetDataSourceLoadingInfo
from openapi_client.models.mock_meta_data import MockMetaData
from openapi_client.models.mock_meta_data_with_type import MockMetaDataWithType
from openapi_client.models.multi_line_string import MultiLineString
from openapi_client.models.multi_point import MultiPoint
from openapi_client.models.multi_polygon import MultiPolygon
from openapi_client.models.none_ogr_source_dataset_time_type import NoneOgrSourceDatasetTimeType
from openapi_client.models.number_param import NumberParam
from openapi_client.models.ogr_meta_data import OgrMetaData
from openapi_client.models.ogr_meta_data_with_type import OgrMetaDataWithType
from openapi_client.models.ogr_source_column_spec import OgrSourceColumnSpec
from openapi_client.models.ogr_source_dataset import OgrSourceDataset
from openapi_client.models.ogr_source_dataset_time_type import OgrSourceDatasetTimeType
from openapi_client.models.ogr_source_duration_spec import OgrSourceDurationSpec
from openapi_client.models.ogr_source_error_spec import OgrSourceErrorSpec
from openapi_client.models.ogr_source_time_format import OgrSourceTimeFormat
from openapi_client.models.order_by import OrderBy
from openapi_client.models.over_under_colors import OverUnderColors
from openapi_client.models.palette_colorizer import PaletteColorizer
from openapi_client.models.permission import Permission
from openapi_client.models.permission_request import PermissionRequest
from openapi_client.models.plot import Plot
from openapi_client.models.plot_output_format import PlotOutputFormat
from openapi_client.models.plot_query_rectangle import PlotQueryRectangle
from openapi_client.models.plot_result_descriptor import PlotResultDescriptor
from openapi_client.models.plot_result_descriptor_with_type import PlotResultDescriptorWithType
from openapi_client.models.plot_update import PlotUpdate
from openapi_client.models.point_symbology import PointSymbology
from openapi_client.models.point_symbology_with_type import PointSymbologyWithType
from openapi_client.models.polygon_symbology import PolygonSymbology
from openapi_client.models.polygon_symbology_with_type import PolygonSymbologyWithType
from openapi_client.models.project import Project
from openapi_client.models.project_filter import ProjectFilter
from openapi_client.models.project_filter_one_of import ProjectFilterOneOf
from openapi_client.models.project_filter_one_of1 import ProjectFilterOneOf1
from openapi_client.models.project_filter_one_of_name import ProjectFilterOneOfName
from openapi_client.models.project_layer import ProjectLayer
from openapi_client.models.project_listing import ProjectListing
from openapi_client.models.project_resource import ProjectResource
from openapi_client.models.project_resource_id import ProjectResourceId
from openapi_client.models.project_version import ProjectVersion
from openapi_client.models.provenance import Provenance
from openapi_client.models.provenance_entry import ProvenanceEntry
from openapi_client.models.provenance_output import ProvenanceOutput
from openapi_client.models.provider_layer_collection_id import ProviderLayerCollectionId
from openapi_client.models.provider_layer_id import ProviderLayerId
from openapi_client.models.quota import Quota
from openapi_client.models.raster_data_type import RasterDataType
from openapi_client.models.raster_dataset_from_workflow import RasterDatasetFromWorkflow
from openapi_client.models.raster_dataset_from_workflow_result import RasterDatasetFromWorkflowResult
from openapi_client.models.raster_properties_entry_type import RasterPropertiesEntryType
from openapi_client.models.raster_properties_key import RasterPropertiesKey
from openapi_client.models.raster_query_rectangle import RasterQueryRectangle
from openapi_client.models.raster_result_descriptor import RasterResultDescriptor
from openapi_client.models.raster_result_descriptor_with_type import RasterResultDescriptorWithType
from openapi_client.models.raster_stream_websocket_result_type import RasterStreamWebsocketResultType
from openapi_client.models.raster_symbology import RasterSymbology
from openapi_client.models.raster_symbology_with_type import RasterSymbologyWithType
from openapi_client.models.resource import Resource
from openapi_client.models.resource_id import ResourceId
from openapi_client.models.rgba_colorizer import RgbaColorizer
from openapi_client.models.role import Role
from openapi_client.models.role_description import RoleDescription
from openapi_client.models.running_task_status import RunningTaskStatus
from openapi_client.models.st_rectangle import STRectangle
from openapi_client.models.server_info import ServerInfo
from openapi_client.models.spatial_partition2_d import SpatialPartition2D
from openapi_client.models.spatial_reference_authority import SpatialReferenceAuthority
from openapi_client.models.spatial_reference_specification import SpatialReferenceSpecification
from openapi_client.models.spatial_resolution import SpatialResolution
from openapi_client.models.start_duration_ogr_source_dataset_time_type import StartDurationOgrSourceDatasetTimeType
from openapi_client.models.start_end_ogr_source_dataset_time_type import StartEndOgrSourceDatasetTimeType
from openapi_client.models.start_ogr_source_dataset_time_type import StartOgrSourceDatasetTimeType
from openapi_client.models.static_color_param import StaticColorParam
from openapi_client.models.static_number_param import StaticNumberParam
from openapi_client.models.stroke_param import StrokeParam
from openapi_client.models.symbology import Symbology
from openapi_client.models.task_abort_options import TaskAbortOptions
from openapi_client.models.task_filter import TaskFilter
from openapi_client.models.task_list_options import TaskListOptions
from openapi_client.models.task_response import TaskResponse
from openapi_client.models.task_status import TaskStatus
from openapi_client.models.task_status_with_id import TaskStatusWithId
from openapi_client.models.text_symbology import TextSymbology
from openapi_client.models.time_granularity import TimeGranularity
from openapi_client.models.time_reference import TimeReference
from openapi_client.models.time_step import TimeStep
from openapi_client.models.time_step_with_type import TimeStepWithType
from openapi_client.models.typed_geometry import TypedGeometry
from openapi_client.models.typed_geometry_one_of import TypedGeometryOneOf
from openapi_client.models.typed_geometry_one_of1 import TypedGeometryOneOf1
from openapi_client.models.typed_geometry_one_of2 import TypedGeometryOneOf2
from openapi_client.models.typed_geometry_one_of3 import TypedGeometryOneOf3
from openapi_client.models.typed_operator import TypedOperator
from openapi_client.models.typed_operator_operator import TypedOperatorOperator
from openapi_client.models.typed_result_descriptor import TypedResultDescriptor
from openapi_client.models.unitless_measurement import UnitlessMeasurement
from openapi_client.models.unix_time_stamp_ogr_source_time_format import UnixTimeStampOgrSourceTimeFormat
from openapi_client.models.unix_time_stamp_type import UnixTimeStampType
from openapi_client.models.update_project import UpdateProject
from openapi_client.models.update_quota import UpdateQuota
from openapi_client.models.upload_file_layers_response import UploadFileLayersResponse
from openapi_client.models.upload_files_response import UploadFilesResponse
from openapi_client.models.user_credentials import UserCredentials
from openapi_client.models.user_info import UserInfo
from openapi_client.models.user_registration import UserRegistration
from openapi_client.models.user_session import UserSession
from openapi_client.models.vector_column_info import VectorColumnInfo
from openapi_client.models.vector_data_type import VectorDataType
from openapi_client.models.vector_query_rectangle import VectorQueryRectangle
from openapi_client.models.vector_result_descriptor import VectorResultDescriptor
from openapi_client.models.vector_result_descriptor_with_type import VectorResultDescriptorWithType
from openapi_client.models.volume import Volume
from openapi_client.models.wcs_boundingbox import WcsBoundingbox
from openapi_client.models.wcs_service import WcsService
from openapi_client.models.wcs_version import WcsVersion
from openapi_client.models.wfs_service import WfsService
from openapi_client.models.wfs_version import WfsVersion
from openapi_client.models.wms_service import WmsService
from openapi_client.models.wms_version import WmsVersion
from openapi_client.models.workflow import Workflow
from openapi_client.models.wrapped_plot_output import WrappedPlotOutput
from openapi_client.models.zero_ogr_source_duration_spec import ZeroOgrSourceDurationSpec
