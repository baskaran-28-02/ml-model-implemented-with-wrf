import xarray as xr
import matplotlib.pyplot as plt
import numpy as np


def view_wind_speed(file_path: str, title: str = "Wind Speed", img_path: str = "images/"):
    ds = xr.open_dataset(file_path)
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
    plt.title(title)

    # Save image using title (replace spaces to avoid issues)
    filename = title.replace(" ", "_").lower() + ".png"
    plt.savefig(img_path+"nested_two_way_one_input_"+filename, dpi=300, bbox_inches="tight")
    print(f"Wind speed map saved as {filename}")
    plt.show()