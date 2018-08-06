import numpy as np
from dps.utils.tf import MLP
from auto_yolo import envs

readme = "Testing yolo_air."

distributions = None

durations = dict(
    long=dict(
        max_hosts=1, ppn=6, cpp=2, gpu_set="0,1", wall_time="24hours",
        project="rpp-bengioy", cleanup_time="20mins",
        slack_time="5mins", n_repeats=6, step_time_limit="24hours"),

    build=dict(
        max_hosts=1, ppn=1, cpp=2, gpu_set="0", wall_time="2hours",
        project="rpp-bengioy", cleanup_time="2mins",
        slack_time="2mins", n_repeats=1, step_time_limit="2hours",
        config=dict(do_train=False)),

    short=dict(
        max_hosts=1, ppn=2, cpp=2, gpu_set="0", wall_time="20mins",
        project="rpp-bengioy", cleanup_time="1mins",
        slack_time="1mins", n_repeats=1, n_param_settings=4),

    oak=dict(
        host_pool=[":"], kind="parallel",
        max_hosts=1, ppn=2, cpp=2, gpu_set="0", wall_time="1hour",
        project="rpp-bengioy", cleanup_time="1mins", slack_time="1mins",
        step_time_limit="1hour", n_repeats=10, n_param_settings=1,
        config=dict(max_steps=4000)),
)

config = dict(
    background_cfg=dict(mode="learn", A=1),
    build_background_encoder=lambda scope: MLP([10, 10], scope=scope),
    build_background_decoder=lambda scope: MLP([10, 10], scope=scope),
    # background_cfg=dict(mode="colour", colour="white"),
    obj_logit_scale=1.0,
    alpha_logit_scale=1.0,
    alpha_logit_bias=1.0,
    obj_temp=1.0,
    # training_wheels=0.0,
    hw_prior_mean=np.log(.33 / .67),
    hw_prior_std=1.0,
    max_steps=10000000,
    patience=10000000,
    final_count_prior_log_odds=0.1,
    postprocessing="random",

    n_train=70000,
    clevr_background_mode="mean",
    tile_shape=(48, 48),
    image_shape=(80, 120),
    pixels_per_cell=(12, 12),
    # clevr_background_mode=None,
    # tile_shape=(96, 96),
    # image_shape=(160, 240),
    # pixels_per_cell=(24, 24),
    object_shape=(28, 28),
)

envs.run_experiment(
    "test_clevr", config, readme, alg="yolo_air",
    task="clevr", durations=durations, distributions=distributions,
)