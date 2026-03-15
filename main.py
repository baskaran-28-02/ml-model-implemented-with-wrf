from test import rain_fall_test_with_wrf_out

if __name__ == "__main__":
    # test cumulative rainfall between 2016-10-06_00:00:00 to 2016-10-06_03:00:00 in the western Atlantic Ocean, roughly:
    #                         * east of Florida
    #                         * north of the Bahamas
    #                         * west of Bermuda
    #                         * in the region where Hurricane Matthew (2016) was active
    rain_fall_test_with_wrf_out.test_rainfall_three_hour()