
import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# ==========================
# WIND ALERT TEST CASES
# ==========================

def test_calm_wind():
    assert wind_alert(10) == "none"

def test_wind_advisory():
    assert wind_alert(39) == "advisory"

def test_wind_watch():
    assert wind_alert(62) == "watch"

def test_wind_warning():
    assert wind_alert(89) == "warning"


# ==========================
# RAIN ALERT TEST CASES
# ==========================

def test_no_rain_alert():
    assert rain_alert(5, False) == "none"

def test_rain_advisory():
    assert rain_alert(10, False) == "advisory"

def test_rain_watch_saturated():
    assert rain_alert(10, True) == "watch"

def test_rain_watch_heavy():
    assert rain_alert(50, False) == "watch"

def test_rain_warning():
    assert rain_alert(50, True) == "warning"


# ==========================
# HEAT ALERT TEST CASES
# ==========================

def test_no_heat_alert():
    assert heat_alert(25, 30) == "none"

def test_heat_advisory():
    assert heat_alert(35, 40) == "advisory"

def test_heat_watch():
    assert heat_alert(40, 40) == "watch"

def test_heat_warning():
    assert heat_alert(45, 40) == "warning"

def test_heat_high_humidity():
    assert heat_alert(34, 60) == "advisory"


# ==========================
# OVERALL ALERT TEST CASES
# ==========================

def test_no_alerts():
    assert overall_alert([]) == "none"

def test_single_alert():
    assert overall_alert(["advisory"]) == "advisory"

def test_highest_alert():
    assert overall_alert(["advisory", "warning", "watch"]) == "warning"

def test_unknown_alert():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])
