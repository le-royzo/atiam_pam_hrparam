
import pandas as pd
import numpy as np
import numpy.typing as npt


def make_modetime_dataframe(data: npt.NDArray[float], n: npt.NDArray[int], t: npt.NDArray[float]) -> npt.NDArray:
    """
    see: https://moonbooks.org/Articles/How-to-store-a-multidimensional-matrix-in-a-dataframe-with-pandas-/

    Args:
        data (npt.NDArray[float]): [description]
        n (npt.NDArray[int]): [description]
        t (npt.NDArray[float]): [description]

    Returns:
        npt.NDArray: [description]
    """
    df_indices = pd.MultiIndex.from_product([n, t], names=["n", "t"])
    data = np.repeat(data, len(t), axis=0)
    df = pd.DataFrame(data=data, index=df_indices, columns=t)
    return df


def cartesian_product(*arrays):
    """[summary]
    Taken from: https://stackoverflow.com/a/11146645 
    Returns:
        [type]: [description]
    """
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[..., i] = a
    return arr.reshape(-1, la)