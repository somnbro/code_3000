import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """

    quasi = ['age', 'zip3', 'gender']
    anon_count = anon_df.groupby(quasi)['anon_id'].transform('count') 
    aux_count = aux_df.groupby(quasi)['name'].transform('count')

    anon_un = anon_df[anon_count == 1] 
    aux_un = aux_df[aux_count == 1]

    matching = pd.merge(anon_un, aux_un, on=quasi)


    final = matching[['anon_id','name']].rename(columns={'name': 'matched_name'})

    return final



    raise NotImplementedError


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    fraction = (len(matches_df) / len(anon_df))

    return fraction

    raise NotImplementedError
