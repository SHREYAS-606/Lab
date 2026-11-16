
import pytest
from weather_alert import wind_alert, rain_alert, heat_alert, overall_alert


# ==========================
# WIND ALERT - BOTH BRANCHES
# ==========================

def test_wind_below_advisory():
    assert wind_alert(38) == "none"

def test_wind_advisory_boundary():
    assert wind_alert(39) == "advisory"

def test_wind_below_watch():
    assert wind_alert(61) == "advisory"

def test_wind_watch_boundary():
    assert wind_alert(62) == "watch"

def test_wind_below_warning():
    assert wind_alert(88) == "watch"

def test_wind_warning_boundary():
    assert wind_alert(89) == "warning"


# ==========================
# RAIN ALERT - BOTH BRANCHES
# ==========================

def test_rain_below_10():
    assert rain_alert(9, False) == "none"

def test_rain_below_50():
    assert rain_alert(10, False) == "advisory"

def test_rain_advisory_saturated():
    assert rain_alert(10, True) == "watch"

def test_rain_heavy_not_saturated():
    assert rain_alert(50, False) == "watch"

def test_rain_heavy_saturated():
    assert rain_alert(50, True) == "warning"


# ==========================
# HEAT ALERT - BOTH BRANCHES
# ==========================

def test_heat_humidity_not_above_40():
    assert heat_alert(35, 40) == "advisory"

def test_heat_humidity_above_40():
    assert heat_alert(34, 60) == "advisory"

def test_heat_below_35():
    assert heat_alert(34, 40) == "none"

def test_heat_below_40():
    assert heat_alert(35, 40) == "advisory"

def test_heat_below_45():
    assert heat_alert(40, 40) == "watch"

def test_heat_warning():
    assert heat_alert(45, 40) == "warning"


# ==========================
# OVERALL ALERT - BOTH BRANCHES
# ==========================

def test_empty_alert_list():
    assert overall_alert([]) == "none"

def test_alert_severity_increases():
    assert overall_alert(["advisory", "watch"]) == "watch"

def test_alert_severity_does_not_increase():
    assert overall_alert(["warning", "advisory"]) == "warning"

def test_invalid_alert():
    with pytest.raises(ValueError, match="unknown alert"):
        overall_alert(["invalid"])
