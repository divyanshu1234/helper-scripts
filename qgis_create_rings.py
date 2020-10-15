"""
To be run using the QGIS Python plugin. Creates rings in the base layer using
the features defined in the feature layers.

Note:
	- base_layer should containt a single polygon feature that encloses the
	  all the features from the feature layers
"""

base_layer_name = 'base_layer'
feature_layer_name_list = ['feature_layer_1', 'feature_layer_2', 'feature_layer_3']

base_layer = QgsProject.instance().mapLayersByName(base_layer_name)[0]
base_feature = base_layer.getFeatures().__next__()

# Stores the geometry with rings
ring_base_geom = base_feature.geometry()

# Adding rings using features to the new geometry object
for feature_layer_name in feature_layer_name_list:
    print(feature_layer_name)
    feature_layer = QgsProject.instance().mapLayersByName(feature_layer_name)[0]

    for feature in feature_layer.getFeatures():
        ring_base_geom.addRing(feature.geometry().asPolygon()[0])

# Deleting the feature with no rings from the base_layer
base_layer.dataProvider().deleteFeatures([base_feature.id()])

# Creating and adding feature with rings to the base_layer
new_base_feature = QgsFeature()
new_base_feature.setGeometry(ring_base_geom)
base_layer.dataProvider().addFeatures([new_base_feature])

# Updating the UI
base_layer.triggerRepaint()
