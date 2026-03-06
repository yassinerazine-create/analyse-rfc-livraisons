def composants_multi_rfc(df):

    result = (
        df.groupby("Composant_Version")["RFC"]
        .nunique()
        .reset_index()
    )

    return result[result["RFC"] > 1]


def rfc_par_livraison(df):

    result = (
        df.groupby("Label Livraison affecté")["RFC"]
        .nunique()
        .reset_index()
    )

    return result
