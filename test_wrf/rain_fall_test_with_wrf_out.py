import xarray as xr
import matplotlib.pyplot as plt

file1 = r"/home/anuruththan/WRF/WRF/test/em_real/wrfout_d01_2016-10-06_00:00:00"
file2 = r"/home/anuruththan/WRF/WRF/test/em_real/wrfout_d01_2016-10-06_03:00:00"

ds1 = xr.open_dataset(file1)
ds2 = xr.open_dataset(file2)


def test_rainfall_three_hour():
    rain1 = ds1["RAINC"].isel(Time=0) + ds1["RAINNC"].isel(Time=0)
    rain2 = ds2["RAINC"].isel(Time=0) + ds2["RAINNC"].isel(Time=0)

    rain_3h = rain2 - rain1

    lats = ds2["XLAT"].isel(Time=0)
    lons = ds2["XLONG"].isel(Time=0)

    plt.figure(figsize=(10, 6))
    plt.pcolormesh(lons, lats, rain_3h, shading="auto")
    plt.colorbar(label="3-hour Rainfall (mm)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("3-hour Rainfall")
    plt.show()