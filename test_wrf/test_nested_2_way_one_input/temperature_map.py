import xarray as xr
import matplotlib.pyplot as plt

file_path = "/home/anuruththan/WRF/WRF/test/em_real/wrfout_d01_2016-10-06_00:00:00"

ds = xr.open_dataset(file_path)

def view_temperature():
    t2_c = ds["T2"].isel(Time=0) - 273.15
    lats = ds["XLAT"].isel(Time=0)
    lons = ds["XLONG"].isel(Time=0)

    plt.figure(figsize=(10, 6))
    plt.pcolormesh(lons, lats, t2_c, shading="auto")
    plt.colorbar(label="2 m Temperature (°C)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Nested Domain Temperature")
    plt.show()