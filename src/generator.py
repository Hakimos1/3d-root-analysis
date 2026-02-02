import trimesh
import json
import os

def create_root_twin(length_mm, radius_mm):
    #creating simple cylinder
    root = trimesh.creation.cylinder(radius=radius_mm, height=length_mm)
    
    #  truth data defined by me
    stats = {
        "length": length_mm,
        "volume": root.volume,
        "branches": 0
    }
    
    #save model and data seperately
    root.export("data/root_model.obj")
    
    with open("data/root_data.json", "w") as f:
        json.dump(stats, f, indent=4)
    
    print(f"Digital Twin erstellt: {length_mm}mm lang.")

if __name__ == "__main__":
    if not os.path.exists("data"):
        os.makedirs("data")
        
    create_root_twin(length_mm=100, radius_mm=2)