"""rio-tiler constant values."""

import multiprocessing
import os

import morecantile
from rasterio.crs import CRS

MAX_THREADS = int(os.environ.get("MAX_THREADS", multiprocessing.cpu_count() * 5))

WEB_MERCATOR_CRS = CRS.from_epsg(3857)
WGS84_CRS = CRS.from_epsg(4326)

WEB_MERCATOR_TMS = morecantile.tms.get("WebMercatorQuad")
