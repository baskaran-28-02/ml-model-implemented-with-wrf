from test_wrf.rain_fall_test_with_wrf_out import test_rainfall_three_hour
from test_wrf.test_nested_2_way_one_input.wind_speed_map import view_wind_speed
from test_wrf.test_nested_2_way_one_input.temperature_map import view_temperature
from test_wrf.test_nested_2_way_one_input.rainfall_map import view_rainfall


if __name__ == "__main__":
    # test_wrf cumulative rainfall between 2016-10-06_00:00:00 to 2016-10-06_03:00:00 in the western Atlantic Ocean, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    test_rainfall_three_hour()
    view_rainfall()
    view_temperature()
    view_wind_speed()