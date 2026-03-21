import xarray as xr
import matplotlib.pyplot as plt


def view_rainfall(file_path: str, file_path_2: str, title: str = "Rainfall", img_path: str = "images/"):
    ds1 = xr.open_dataset(file_path)
    ds2 = xr.open_dataset(file_path_2)

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
    plt.title(title)

    # Save image using title (replace spaces to avoid issues)
    filename = title.replace(" ", "_").lower() + ".png"
    plt.savefig(img_path+"nested_two_way_one_input_"+filename, dpi=300, bbox_inches="tight")
    print(f"Rainfall map saved as {filename}")

    plt.show()