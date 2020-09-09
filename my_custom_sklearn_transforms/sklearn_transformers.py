from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        data = pd.get_dummies(data,columns=["OBJETIVO"])
        data = data.drop(['OBJETIVO_Sospechoso'],axis=1)
        cabecera = [
            'EFECTIVO',
            'CXC',
            'INVENTARIO',
            'EQ_OFICINA',
            'EQ_TRANSPORTE',
            'TERRENOS_Y_CONSTRUCCIONES',
            'CXP',
            'CONTRIBUCIONES_X_PAGAR',
            'ANTICIPOS_CTE',
            'CAP_SOCIAL',
            'UTILIDADES_ACUMULADAS',
            'UTILIDAD_O_PERDIDA',
            'TOTAL_VENTAS',
            'TOTAL_COMPRAS',
            'UTILIDAD_BRUTA',
            'TOTAL_GASTOS',
            'OBJETIVO'
        ]
        data.columns = cabecera
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
