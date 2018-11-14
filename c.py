try:
    print(1/0)
except Exception as e:
    raise RuntimeError("Something bad happened") from e
