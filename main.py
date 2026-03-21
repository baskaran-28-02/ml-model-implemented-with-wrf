from test_wrf.rain_fall_test_with_wrf_out import test_rainfall_three_hour
from test_wrf.test_nested_2_way_one_input.wind_speed_map import view_wind_speed
from test_wrf.test_nested_2_way_one_input.temperature_map import view_temperature
from test_wrf.test_nested_2_way_one_input.rainfall_map import view_rainfall


file_path_nest = "/home/anuruththan/WRF/WRF/test/em_real/wrfout_d02_2016-10-06_00:00:00"
file_path_nest_2 = "/home/anuruththan/WRF/WRF/test/em_real/wrfout_d02_2016-10-06_03:00:00"

file_path = r"/home/anuruththan/WRF/WRF/test/em_real/wrfout_d01_2016-10-06_00:00:00"
file_path_2 = r"/home/anuruththan/WRF/WRF/test/em_real/wrfout_d01_2016-10-06_03:00:00"

img_path = "images/nested_two_way_one_input/"

if __name__ == "__main__":
    # test_wrf cumulative rainfall between 2016-10-06_00:00:00 to 2016-10-06_03:00:00 in the western Atlantic Ocean, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    view_rainfall(file_path, file_path_2, "3-hour Rainfall Differance", img_path)

    # test_wrf cumulative rainfall between 2016-10-06_00:00:00 to 2016-10-06_03:00:00 in the western Atlantic Ocean for nested domain, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    view_rainfall(file_path_nest, file_path_nest_2, "Nested Domain 3-hour Rainfall", img_path)

    # test_wrf cumulative temperature on 2016-10-06_00:00:00 in the western Atlantic Ocean, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    view_temperature(file_path, "Temperature", img_path)

    # test_wrf cumulative temperature on 2016-10-06_00:00:00 in the western Atlantic Ocean for nested domain, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    view_temperature(file_path_nest, "Nested Domain Temperature", img_path)

    # test_wrf cumulative wind speed on 2016-10-06_00:00:00 in the western Atlantic Ocean, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    view_wind_speed(file_path, "Wind Speed", img_path)

    # test_wrf cumulative wind speed on 2016-10-06_00:00:00 in the western Atlantic Ocean for nested domain, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    view_wind_speed(file_path_nest,"Nested Domain Wind Speed", img_path)