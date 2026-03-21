import xarray as xr
import matplotlib.pyplot as plt


def view_temperature(file_path: str, title: str = "Temperature", img_path: str = "images/"):
    ds = xr.open_dataset(file_path)

    t2_c = ds["T2"].isel(Time=0) - 273.15
    lats = ds["XLAT"].isel(Time=0)
    lons = ds["XLONG"].isel(Time=0)

    plt.figure(figsize=(10, 6))
    plt.pcolormesh(lons, lats, t2_c, shading="auto")
    plt.colorbar(label="2 m Temperature (°C)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.title("Nested Domain Temperature")

    # Save image using title (replace spaces to avoid issues)
    filename = title.replace(" ", "_").lower() + ".png"
    plt.savefig(img_path+"nested_two_way_one_input_"+filename, dpi=300, bbox_inches="tight")
    print(f"Temperature map saved as {filename}")

    plt.show()