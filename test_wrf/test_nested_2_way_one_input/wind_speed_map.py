import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

file_path = "/home/anuruththan/WRF/WRF/test/em_real/wrfout_d01_2016-10-06_00:00:00"

ds = xr.open_dataset(file_path)

def view_wind_speed():
    u10 = ds["U10"].isel(Time=0)
    v10 = ds["V10"].isel(Time=0)
    wind = np.sqrt(u10**2 + v10**2)

    lats = ds["XLAT"].isel(Time=0)
    lons = ds["XLONG"].isel(Time=0)

    plt.figure(figsize=(10, 6))
    plt.pcolormesh(lons, lats, wind, shading="auto")
    plt.colorbar(label="10 m Wind Speed (m/s)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Nested Domain Wind Speed")
    plt.show()