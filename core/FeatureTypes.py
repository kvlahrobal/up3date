class FeatureTypes:
    featuretypes = {
        "building": {
            "Building": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "BuildingPart": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "BuildingInstallation": {
                "lod": [1,2,3,4,5],
                "color": "#ae825a"
            },
            "IntBuildingInstallation": {
                "lod": [1,2,3,4,5],
                "color": "#ae825a"
            },
            "RoofSurface": {
                "lod": [1,2,3,4,5],
                "color": "#9c4444"
            },
            "WallSurface": {
                "lod": [1,2,3,4,5],
                "color": "#dbdbdb"
            },
            "GroundSurface": {
                "lod": [1,2,3,4,5],
                "color": "#747474"
            },
            "ClosureSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "FloorSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "OuterFloorSurface": {
                "lod": [1,2,3,4,5],
                "color": "#854c7b"
            },
            "CeilingSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "OuterCeilingSurface": {
                "lod": [1,2,3,4,5],
                "color": "#7e7d54"
            },
            "Door": {
                "lod": [4,5],
                "color": "#4d4de8"
            },
            "Window": {
                "lod": [4,5],
                "color": "#80c7c8"
            },
            "Room": {
                "lod": [5],
                "color": "#ffffff"
            },
            "BuildingFurniture": {
                "lod": [5],
                "color": "#ffffff"
            },
        },
        "bridge":{
            "Bridge": {
                "lod": [1,2,3,4,5],
                "color": "#a77600"
            },
            "BridgePart": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "BridgeInstallation": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "IntBridgeInstallation": {
                "lod": [1,2,3,4,5],
                "color": "#7e7d54"
            },
            "BridgeConstructionElement": {
                "lod": [1,2,3,4,5],
                "color": "#7737ae"
            },
            "RoofSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "WallSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "GroundSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "ClosureSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "FloorSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "OuterFloorSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "InteriorWallSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "CeilingSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "OuterCeilingSurface": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "Door": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "Window": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "BridgeRoom": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            },
            "BridgeFurniture": {
                "lod": [1,2,3,4,5],
                "color": "#ffffff"
            }
        }
    }

    def getAllElementsOfFeatureType(self, type):
        return self.featuretypes[type]

    def getAllLODs(self):
        pass

    def getAllFeatures(self):
        print(list(self.featuretypes))
        return list(self.featuretypes)
    
    def getRGBColor(self, construction, surface):
        rgb = self.hexToRGB(self.featuretypes[construction][surface]["color"])
        return rgb
    
    def hexToRGB(self, value):
        value = value.replace("#","")
        rgb = tuple(int(value[i:i+2], 16) for i in (0, 2, 4))
        return rgb