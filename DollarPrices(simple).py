import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------------------------------------------------
year = [1357, 1358, 1359, 1360, 1361, 1362, 1363, 1364, 1365, 1366, 1367, 1368, 1369, 1370, 1371, 1372, 1373, 1374, 1375
        , 1376, 1377, 1378, 1379, 1380, 1381, 1382, 1383, 1384, 1385, 1386, 1387, 1388, 1389, 1390, 1391, 1392, 1393
        , 1394, 1395, 1396, 1397, 1398, 1399, 1400, 1401]
price = [10, 14, 20, 27, 35, 45, 58, 61, 74, 99, 96, 120, 141, 142, 149, 180, 263, 403, 444, 478, 646, 863, 813, 792,
         799, 832, 874, 904, 922, 935, 966, 1000, 1100, 1800, 3800, 3600, 3550, 3600, 3425, 4250, 15067, 15757, 23700,
         27000, 42000]
# ----------------------------------------------------------------------------------------------------------------------


plt.plot(year, price, color='green')
plt.show()  # simple plot (not recommended)