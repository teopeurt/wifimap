
Page.registerLoadUrl("^/$", SpotListPage.load);

Page.registerLoadUrl("^/spots/add$", AddSpotPage.load);
Page.registerUnloadUrl("^/spots/add$", AddSpotPage.unload);