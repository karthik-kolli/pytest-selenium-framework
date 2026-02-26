COMMON_OPTIONS ={
    "headless":"--headless",
    "disable_gpu" : "--disable-gpu",
}

WINDOW_OPTIONS={
    "start-maximized":"--start-maximized",
}

SECURITY_OPTIONS={
  "no_sandbox":"--no-sandbox"
}

OPTION_MAP={
    **COMMON_OPTIONS,
    **WINDOW_OPTIONS,
    **SECURITY_OPTIONS
}

