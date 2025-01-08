# Part 4 Solution
fig, ax = plt.subplots(figsize=(10, 10))

norm2 = simple_norm(data, 'sqrt', percent=99)
axim = ax.imshow(data, norm=norm2)

xypos = zip(brightest3['x_fit'], brightest3['y_fit'])
aper = CircularAperture(xypos, r=10)
patches = aper.plot(color='red')
