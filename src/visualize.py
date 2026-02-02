import trimesh

def show_model(file_path):
    try:
        # load model
        mesh = trimesh.load(file_path)
        
        # validation output
        print(f"Modell geladen: {file_path}")
        print(f"Anzahl der Flächen (Faces): {len(mesh.faces)}")
        
    
        mesh.show()
        
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    # display model created by generator
    path_to_model = "data/root_model.obj"
    show_model(path_to_model)