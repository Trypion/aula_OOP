x0, y0, x1, y1 = [int(w) for w in input().split()]
r1 = {"x0": x0, "y0": y0, "x1": x1, "y1": y1}
x0, y0, x1, y1 = [int(w) for w in input().split()]
r2 = {"x0": x0, "y0": y0, "x1": x1, "y1": y1}

if (r1["x0"] < r2["x1"] and
    r1["x1"] > r2["x0"] and
    r1["y0"] < r2["y1"] and
    r1["y1"] > r2["y0"]
    ):
    print(1)
else:
    print(0) 
