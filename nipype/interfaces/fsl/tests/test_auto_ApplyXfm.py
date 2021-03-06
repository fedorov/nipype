# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.fsl.preprocess import ApplyXfm
def test_ApplyXfm_inputs():
    input_map = dict(rigid2D=dict(argstr='-2D',
    ),
    in_matrix_file=dict(argstr='-init %s',
    ),
    verbose=dict(argstr='-verbose %d',
    ),
    reference=dict(position=1,
    mandatory=True,
    argstr='-ref %s',
    ),
    padding_size=dict(units='voxels',
    argstr='-paddingsize %d',
    ),
    sinc_window=dict(argstr='-sincwindow %s',
    ),
    interp=dict(argstr='-interp %s',
    ),
    wmnorms=dict(argstr='-wmnorms %s',
    min_ver='5.0.0',
    ),
    coarse_search=dict(units='degrees',
    argstr='-coarsesearch %d',
    ),
    no_resample=dict(argstr='-noresample',
    ),
    sinc_width=dict(units='voxels',
    argstr='-sincwidth %d',
    ),
    in_weight=dict(argstr='-inweight %s',
    ),
    fieldmap=dict(argstr='-fieldmap %s',
    min_ver='5.0.0',
    ),
    echospacing=dict(argstr='-echospacing %f',
    min_ver='5.0.0',
    ),
    ref_weight=dict(argstr='-refweight %s',
    ),
    apply_isoxfm=dict(xor=['apply_xfm'],
    argstr='-applyisoxfm %f',
    ),
    fieldmapmask=dict(argstr='-fieldmapmask %s',
    min_ver='5.0.0',
    ),
    in_file=dict(position=0,
    mandatory=True,
    argstr='-in %s',
    ),
    bbrtype=dict(min_ver='5.0.0',
    argstr='-bbrtype %s',
    ),
    no_clamp=dict(argstr='-noclamp',
    ),
    force_scaling=dict(argstr='-forcescaling',
    ),
    pedir=dict(argstr='-pedir %d',
    min_ver='5.0.0',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    display_init=dict(argstr='-displayinit',
    ),
    schedule=dict(argstr='-schedule %s',
    ),
    args=dict(argstr='%s',
    ),
    uses_qform=dict(argstr='-usesqform',
    ),
    wmcoords=dict(argstr='-wmcoords %s',
    min_ver='5.0.0',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    fine_search=dict(units='degrees',
    argstr='-finesearch %d',
    ),
    angle_rep=dict(argstr='-anglerep %s',
    ),
    no_search=dict(argstr='-nosearch',
    ),
    apply_xfm=dict(requires=['in_matrix_file'],
    argstr='-applyxfm',
    usedefault=True,
    ),
    wm_seg=dict(argstr='-wmseg %s',
    min_ver='5.0.0',
    ),
    out_file=dict(name_source=['in_file'],
    hash_files=False,
    name_template='%s_flirt',
    position=2,
    argstr='-out %s',
    ),
    bbrslope=dict(argstr='-bbrslope %f',
    min_ver='5.0.0',
    ),
    datatype=dict(argstr='-datatype %s',
    ),
    save_log=dict(),
    dof=dict(argstr='-dof %d',
    ),
    out_matrix_file=dict(hash_files=False,
    name_template='%s_flirt.mat',
    name_source=['in_file'],
    keep_extension=True,
    position=3,
    argstr='-omat %s',
    ),
    no_resample_blur=dict(argstr='-noresampblur',
    ),
    min_sampling=dict(units='mm',
    argstr='-minsampling %f',
    ),
    cost_func=dict(argstr='-searchcost %s',
    ),
    cost=dict(argstr='-cost %s',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    searchr_x=dict(units='degrees',
    argstr='-searchrx %s',
    ),
    out_log=dict(name_source=['in_file'],
    keep_extension=True,
    name_template='%s_flirt.log',
    requires=['save_log'],
    ),
    output_type=dict(),
    searchr_z=dict(units='degrees',
    argstr='-searchrz %s',
    ),
    bins=dict(argstr='-bins %d',
    ),
    searchr_y=dict(units='degrees',
    argstr='-searchry %s',
    ),
    )
    inputs = ApplyXfm.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value
def test_ApplyXfm_outputs():
    output_map = dict(out_log=dict(),
    out_file=dict(),
    out_matrix_file=dict(),
    )
    outputs = ApplyXfm.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value
