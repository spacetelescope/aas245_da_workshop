# Part 2 Solution
resid = psfphot.make_residual_image(data)

fig, ax = plt.subplots(figsize=(10, 10))
norm = simple_norm(data, 'sqrt', percent=95)
axim = ax.imshow(resid, norm=norm)
