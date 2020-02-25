""" Tests for daops library """

# FutureWarning: In xarray version 0.15 the default behaviour of `open_mfdataset`
# will change. To retain the existing behavior, pass
# combine='nested'. To use future default behavior, pass
# combine='by_coords'.


def test_subset_data_ref():
    """ Tests daops api.subset function with only a data ref"""
    pass


def test_subset_time():
    """ Tests daops api.subset function with a time subset.
    Check ResultSet contains the correct info"""
    pass

def test_subset_invalid_time():
    """ Tests daops api.subset function with an invalid time subset."""
    pass


def test_subset_space():
    """ Tests daops api.subset function with a space subset.
    Check ResultSet contains the correct info"""
    pass


def test_subset_invalid_space():
    """ Tests daops api.subset function with an invalid space subset."""
    pass


def test_subset_level():
    """ Tests daops api.subset function with a level subset.
    Check ResultSet contains the correct info"""
    pass


def test_subset_invalid_level():
    """ Tests daops api.subset function with an invalid level subset."""
    pass


def test_subset_all():
    """ Tests daops api.subset function with time, space, level subsets.
    Check ResultSet contains the correct info"""
    pass


def test_wrap_sequence_str():
    """ Tests daops utils._wrap_sequence with string.
    Check correct type is returned when string passed. """
    pass


def test_wrap_sequence_not_str():
    """ Tests daops utils._wrap_sequence with object that isn't a string.
    Check correct response when passed. """
    pass


def test_is_data_ref_characterised_true():
    """ Tests daops utils.is_dataref_characterised.
    Check correct response for data ref that is characterised. """
    pass


def test_is_data_ref_characterised_false():
    """ Tests daops utils.is_dataref_characterised.
    Check correct response for data ref that is not characterised. """
    pass


def test_is_characterised_all_required_true_mixed():
    """ Tests daops utils.is_characterised.
    Check response when all required is True for mixed characterisation."""
    pass


def test_is_characterised_all_required_true_all():
    """ Tests daops utils.is_characterised.
    Check response when all required is True for all characterised."""
    pass


def test_is_characterised_all_required_true_none():
    """ Tests daops utils.is_characterised.
    Check response when all required is True for none characterised."""
    pass


def test_is_characterised_all_required_false_mixed():
    """ Tests daops utils.is_characterised.
        Check response when all required is False for mixed characterisation."""
    pass


def test_is_characterised_all_required_false_all():
    """ Tests daops utils.is_characterised.
    Check response when all required is False for all characterised."""
    pass


def test_is_characterised_all_required_false_none():
    """ Tests daops utils.is_characterised.
    Check response when all required is False for none characterised."""
    pass