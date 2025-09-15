# Gaussian-Grouping: 说明文档

## Gaussian Model

在`gaussian-grouping`项目中运行语义Gaussian模型时，需将子模块"gaussian-splatting"中的`scene.gaussian_model`切换为`gaussian_model`。

## GS Simulation

在`gs_simulation.py`中，我们默认使用`PhysGaussian`进行重建的3D Gaussian Splatting场景的模拟。同时，也支持使用全新的`gaussian_model`进行语义Gaussian的实验，配置文件示例见`config/bear.json`。

请先从`gaussian-grouping`中下载语义Gaussian模型，并放置于`model/bear/`目录下。

运行脚本如下：

```bash
python3 gs_simulation.py --model_path ./model/bear/ --output_path output --config ./config/bear.json --render_img --compile_video
```

## GS Simulation 2

与`gs_simulation.py`相比，`gs_simulation_2.py`**删除了选择掩码的部分**，此脚本仅可对目标Gaussian对象进行操作，背景已被去除。

如需获取该对象，请在`gaussian-grouping`中运行`edit_object_removal`，以获得被纯净分割的Gaussian对象。

模拟脚本如下：

```bash
python3 gs_simulation_2.py --model_path ./model/bear/ --output_path output2 --config ./config/bear.json --render_img --compile_video
```


## Utils

- **离群点过滤：**  
  为了过滤Gaussian模型中的离群点，我们在`gaussian_model`中加入了`filter_by_dbscan`功能。你可以通过调整相关超参数来控制过滤强度。

- **自动设置MPM力作用点：**  
  为方便施加MPM力，我们在`gs_simulation`中新增了`auto_set_mpm`方法，能够自动获取目标Gaussian对象的中心附近的位置。
