# Gaussian-Grouping: README

## Gaussian Model

To run the semantic Gaussian model in the `gaussian-grouping` project, you need to use `gaussian_model` from the submodule "gaussian-splatting" instead of the default `scene.gaussian_model`.

## GS Simulation

In `gs_simulation.py`, we simulate a reconstructed 3D Gaussian Splatting scene—by default using `PhysGaussian`. Additionally, we support semantic Gaussian using the new `gaussian_model`. An example configuration can be found at `config/bear.json`.

To use the semantic Gaussian model, download it from `gaussian-grouping` and place it into `model/bear/`.

Run the simulation with:

```bash
python3 gs_simulation.py --model_path ./model/bear/ --output_path output --config ./config/bear.json --render_img --compile_video
```

## GS Simulation 2

Compared to `gs_simulation.py`, `gs_simulation_2.py` **removes the mask selection part**. In this script, you can only operate on the target Gaussian object, which has been isolated from the background.

To obtain this object, run the `edit_object_removal` tool in `gaussian-grouping` to extract a purified, segmented Gaussian object.

Use the following script to run the simulation:

```bash
python3 gs_simulation_2.py --model_path ./model/bear/ --output_path output2 --config ./config/bear.json --render_img --compile_video
```


## Utils

- **Filtering Outliers:**  
  To remove outliers in the Gaussian model, we provide the `filter_by_dbscan` function in `gaussian_model`. You can adjust the hyperparameters to control the filtering strength.

- **Automatically Setting MPM Force Points:**  
  For convenience in MPM force application, we introduce the `auto_set_mpm` function in `gs_simulation`. This automatically selects a point near the center of the target Gaussian object.