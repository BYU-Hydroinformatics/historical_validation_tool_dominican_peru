from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting, SpatialDatasetServiceSetting

class HistoricalValidationToolPeru(TethysAppBase):
    """
    Tethys app class for Historical Validation Tool Peru.
    """

    name = 'Historical Validation Tool Peru'
    index = 'home'
    icon = 'historical_validation_tool_peru/images/historical_validation_peru_logo.jpeg'
    package = 'historical_validation_tool_peru'
    root_url = 'historical-validation-tool-peru'
    color = '#2980b9'
    description = 'This app combines the observed data and the simulated data from the GEOGloWS ECMWF Streaamflow Services in Peru.'
    tags = '"Hydrology", "Time Series", "Bias Correction", "Hydrostats", "GEOGloWS", "Historical Validation Tool", "Peru"'
    enable_feedback = False
    feedback_emails = []
    controller_modules = [ "controllers" ]

    def spatial_dataset_service_settings(self):
        """
		Spatial_dataset_service_settings method.
		"""
        return (
            SpatialDatasetServiceSetting(
                name='main_geoserver',
                description='spatial dataset service for app to use (https://tethys2.byu.edu/geoserver/rest/)',
                engine=SpatialDatasetServiceSetting.GEOSERVER,
                required=True,
            ),
        )

    # def url_maps(self):
    #     """
    #     Add controllers
    #     """
    #     UrlMap = url_map_maker(self.root_url)

    #     url_maps = (
    #         UrlMap(
    #             name='home',
    #             url='historical-validation-tool-peru',
    #             controller='historical_validation_tool_peru.controllers.home'
    #         ),
    #         UrlMap(
    #             name='get_popup_response',
    #             url='get-request-data',
    #             controller='historical_validation_tool_peru.controllers.get_popup_response'
    #         ),
    #         UrlMap(
    #             name='get_hydrographs',
    #             url='get-hydrographs',
    #             controller='historical_validation_tool_peru.controllers.get_hydrographs'
    #         ),
    #         UrlMap(
    #             name='get_dailyAverages',
    #             url='get-dailyAverages',
    #             controller='historical_validation_tool_peru.controllers.get_dailyAverages'
    #         ),
    #         UrlMap(
    #             name='get_monthlyAverages',
    #             url='get-monthlyAverages',
    #             controller='historical_validation_tool_peru.controllers.get_monthlyAverages'
    #         ),
    #         UrlMap(
    #             name='get_scatterPlot',
    #             url='get-scatterPlot',
    #             controller='historical_validation_tool_peru.controllers.get_scatterPlot'
    #         ),
    #         UrlMap(
    #             name='get_scatterPlotLogScale',
    #             url='get-scatterPlotLogScale',
    #             controller='historical_validation_tool_peru.controllers.get_scatterPlotLogScale'
    #         ),
    #         UrlMap(
    #             name='get_volumeAnalysis',
    #             url='get-volumeAnalysis',
    #             controller='historical_validation_tool_peru.controllers.get_volumeAnalysis'
    #         ),
    #         UrlMap(
    #             name='volume_table_ajax',
    #             url='volume-table-ajax',
    #             controller='historical_validation_tool_peru.controllers.volume_table_ajax'
    #         ),
    #         UrlMap(
    #             name='make_table_ajax',
    #             url='make-table-ajax',
    #             controller='historical_validation_tool_peru.controllers.make_table_ajax'
    #         ),
    #         UrlMap(
    #             name='get-available-dates',
    #             url='ecmwf-rapid/get-available-dates',
    #             controller='historical_validation_tool_peru.controllers.get_available_dates'
    #         ),
    #         UrlMap(
    #             name='get-time-series',
    #             url='get-time-series',
    #             controller='historical_validation_tool_peru.controllers.get_time_series'),
    #         UrlMap(
    #             name='get-time-series-bc',
    #             url='get-time-series-bc',
    #             controller='historical_validation_tool_peru.controllers.get_time_series_bc'),
    #         #UrlMap(
    #         #    name='get_observed_discharge_csv',
    #         #    url='get-observed-discharge-csv',
    #         #    controller='historical_validation_tool_peru.controllers.get_observed_discharge_csv'
    #         #),
    #         UrlMap(
    #             name='get_simulated_discharge_csv',
    #             url='get-simulated-discharge-csv',
    #             controller='historical_validation_tool_peru.controllers.get_simulated_discharge_csv'
    #         ),
    #         UrlMap(
    #             name='get_simulated_bc_discharge_csv',
    #             url='get-simulated-bc-discharge-csv',
    #             controller='historical_validation_tool_peru.controllers.get_simulated_bc_discharge_csv'
    #         ),
    #         UrlMap(
    #             name='get_forecast_data_csv',
    #             url='get-forecast-data-csv',
    #             controller='historical_validation_tool_peru.controllers.get_forecast_data_csv'
    #         ),
    #         UrlMap(
    #             name='get_forecast_bc_data_csv',
    #             url='get-forecast-bc-data-csv',
    #             controller='historical_validation_tool_peru.controllers.get_forecast_bc_data_csv'
    #         ),
    #         UrlMap(
    #             name='get_forecast_ensemble_data_csv',
    #             url='get-forecast-ensemble-data-csv',
    #             controller='historical_validation_tool_peru.controllers.get_forecast_ensemble_data_csv'
    #         ),
    #         UrlMap(
    #             name='get_forecast_ensemble_bc_data_csv',
    #             url='get-forecast-ensemble-bc-data-csv',
    #             controller='historical_validation_tool_peru.controllers.get_forecast_ensemble_bc_data_csv'
    #         ),
    #         ########################################################
    #         ########################################################
    #         UrlMap(
    #             name='get_zoom_array',
    #             url='get-zoom-array',
    #             controller='historical_validation_tool_peru.controllers.get_zoom_array',
    #         ),
    #         ########################################################
    #         ########################################################
    #     )

    #     return url_maps

    def custom_settings(self):
        return (
            CustomSetting(
                name='workspace',
                type=CustomSetting.TYPE_STRING,
                description='Workspace within Geoserver where web service is',
                required=True,
                default='peru_hydroviewer',
            ),
            CustomSetting(
                name='region',
                type=CustomSetting.TYPE_STRING,
                description='GESS Region',
                required=True,
                default='south_america-geoglows',
            ),
            CustomSetting(
                name='hydroshare_resource_id',
                type=CustomSetting.TYPE_STRING,
                description='Hydroshare Resource ID',
                required=True,
            ),
            CustomSetting(
                name='username',
                type=CustomSetting.TYPE_STRING,
                description='Hydroshare Username',
                required=True,
            ),
            CustomSetting(
                name='password',
                type=CustomSetting.TYPE_STRING,
                description='Hydroshare Password',
                required=True,
            ),
        )