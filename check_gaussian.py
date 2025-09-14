import sys
sys.path.append("gaussian-splatting")
# Gaussian splatting dependencies
from utils.sh_utils import eval_sh
from scene.gaussian_model import GaussianModel
from diff_gaussian_rasterization import (
    GaussianRasterizationSettings,
    GaussianRasterizer,
)
from scene.cameras import Camera as GSCamera
from gaussian_renderer import render, GaussianModel
from utils.system_utils import searchForMaxIteration
from utils.graphics_utils import focal2fov


sh_degree = 3
checkpt_path = "./model/bear/point_cloud_removal/iteration_30000/point_cloud_removed.ply"
save_path = "./model/bear/point_cloud_removal/iteration_30000/point_cloud_refined.ply"

# Load guassians
gaussians = GaussianModel(sh_degree)
gaussians.load_ply(checkpt_path)
bbox_min, bbox_max, num_points, volume = gaussians.get_stats()
print("过滤前:", bbox_min, bbox_max, num_points, volume)

gaussians.filter_by_dbscan(eps=0.05, min_samples=10)

bbox_min, bbox_max, num_points, volume = gaussians.get_stats()
print("过滤后:", bbox_min, bbox_max, num_points, volume)
gaussians.save_ply(save_path)