# Part 1 Solution
fit_shape = (5, 5)
finder = IRAFStarFinder(threshold=6.0, fwhm=3.0)
psfphot = PSFPhotometry(psf_model, fit_shape, finder=finder,
                        aperture_radius=5, progress_bar=True)
phot = psfphot(data, error=error)
phot
