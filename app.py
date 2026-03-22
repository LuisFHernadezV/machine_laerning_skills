import streamlit as st

st.title("Visión general de algoritmos de Machine Learning")
st.write(
    "Esta aplicación muestra una descripción breve y un fragmento de código de los algoritmos principales que se encuentran en los notebooks del curso."
)

# Define a dictionary with algorithm info
algorithms = {
    "Linear Regression": {
        "description": "Modelo supervisado para predecir una variable continua usando una combinación lineal de características.",
        "math": r"\hat{y}=X\beta, \text{ donde } \beta \text{ son los coeficientes estimados mediante mínimos cuadrados. }",
        "code": """import numpy as np
from sklearn.linear_model import LinearRegression
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + np.random.randn(100) * 0.5
model = LinearRegression()
model.fit(X, y)
print('Coeficientes:', model.coef_, 'Intercept:', model.intercept_)""",
        "image": "images/linear_regression.png",
    },
    "Logistic Regression": {
        "description": "Modelo lineal para clasificación binaria que estima la probabilidad de pertenecer a una clase.",
        "math": r"p = \frac{1}{1 + e^{-X\beta}} \text{, donde p es la probabilidad estimada.}",
        "code": """from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_breast_cancer
X, y = load_breast_cancer(return_X_y=True)
model = LogisticRegression(max_iter=1000)
model.fit(X, y)
print('Exactitud:', model.score(X, y))""",
        "image": "images/logistic_regression.png",
    },
    "Support Vector Machine": {
        "description": "Clasificador que encuentra el hiperplano con el mayor margen entre clases.",
        "math": r"\underset{w,b}{\text{min}}\; \frac{1}{2}\|w\|^2 \;\text{s.a.}\; y_i (w \cdot x_i + b) \ge 1 \text{, optimizando margen}.",
        "code": """from sklearn.svm import SVC
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=200, n_features=20, random_state=42)
clf = SVC(kernel='rbf')
clf.fit(X, y)
print('Exactitud:', clf.score(X, y))""",
        "image": "images/svm.png",
    },
    "Decision Tree": {
        "description": "Modelo de árbol que divide recursivamente los datos según la mejor característica.",
        "math": r"\text{Impureza}(t) = \sum_{c} p(c|t) (1 - p(c|t)) \text{, la división busca minimizar la impureza ponderada de los hijos.}",
        "code": """from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
clf = DecisionTreeClassifier()
clf.fit(X, y)
plot_tree(clf)
plt.show()""",
        "image": "images/decision_tree.png",
    },
    "Random Forest": {
        "description": "Conjunto de árboles de decisión entrenados con muestreo bootstrap y características aleatorias.",
        "math": r"\hat{y} = \frac{1}{B} \sum_{b=1}^{B} T_b(x)",
        "code": """from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
X, y = load_wine(return_X_y=True)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X, y)
print('Exactitud:', clf.score(X, y))""",
        "image": "images/random_forest.png",
    },
    "Isolation Forest": {
        "description": "Algoritmo de detección de anomalías basado en aislar puntos mediante árboles aleatorios.",
        "math": r"c(n) = 2H(n - 1) - \left( \frac{2(n - 1)}{n} \right)",
        "code": """from sklearn.ensemble import IsolationForest
import numpy as np
rng = np.random.RandomState(42)
X = np.r_[rng.normal(0, 0.5, (100, 2)), rng.normal(5, 0.5, (20, 2))]
clf = IsolationForest(contamination=0.1, random_state=42)
clf.fit(X)
labels = clf.predict(X)
print('Número de anomalías detectadas:', (labels == -1).sum())""",
        "image": "images/isolation_forest.png",
    },
    "PCA": {
        "description": "Reducción de dimensionalidad mediante descomposición en componentes principales.",
        "code": """from sklearn.decomposition import PCA
from sklearn.datasets import load_digits
X, _ = load_digits(return_X_y=True)
 pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)
print('Forma reducida:', X_reduced.shape)""",
        "image": "images/pca.png",
    },
    "K-Means": {
        "description": "Algoritmo de clustering que divide los datos en k grupos minimizando la varianza intra-clúster.",
        "math": r"J = \sum_{j=1}^{k} \sum_{x_i \in C_j} \| x_i - \mu_j \|^2",
        "code": """from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=300, centers=4, random_state=42)
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
print('Centroides:', kmeans.cluster_centers_)""",
        "image": "images/kmeans.png",
    },
    "DBSCAN": {
        "description": "Algoritmo de clustering basado en densidad que detecta grupos de forma arbitraria y ruido.",
        "code": """from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
X, _ = make_moons(n_samples=200, noise=0.05, random_state=42)
clustering = DBSCAN(eps=0.2, min_samples=5)
labels = clustering.fit_predict(X)
print('Número de clusters encontrados:', len(set(labels)) - (1 if -1 in labels else 0))""",
        "image": "images/dbscan.png",
    },
    "Naive Bayes": {
        "description": "Clasificador probabilístico basado en la regla de Bayes y suposiciones de independencia.",
        "math": r"P(A|B) = \frac{P(B|A)P(A)}{P(B)} \text{, donde } P(B|A) \text{ es la probabilidad de pertenecer a la clase } B \text{ dado que } A \text{ pertenece a la clase } B.",
        "code": """from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups_vectorized
X, y = fetch_20newsgroups_vectorized(subset='train', return_X_y=True)
clf = MultinomialNB()
clf.fit(X, y)
print('Exactitud:', clf.score(X, y))""",
        "image": "images/naive_bayes.png",
    },
    "Neural Network (MLP)": {
        "description": "Red neuronal de perceptrón multicapa para clasificación o regresión.",
        "math": r"\frac{\partial \mathcal{L}}{\partial W^{[l]}} = \frac{\partial \mathcal{L}}{\partial a^{[l]}} \cdot \frac{\partial a^{[l]}}{\partial z^{[l]}} \cdot \frac{\partial z^{[l]}}{\partial W^{[l]}}",
        "code": """from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_digits
X, y = load_digits(return_X_y=True)
mlp = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300)
mlp.fit(X, y)
print('Exactitud:', mlp.score(X, y))""",
        "image": "images/mlp.png",
    },
}

# Sidebar selection
algo = st.sidebar.selectbox("Selecciona un algoritmo", list(algorithms.keys()))
info = algorithms[algo]

st.header(algo)
st.markdown(f"**Descripción:** {info['description']}")
if info.get("math"):
    st.latex(info["math"])
st.subheader("Código de ejemplo")
st.code(info["code"], language="python")

if info["image"]:
    st.image(info["image"], caption=algo)

st.caption(
    "*Este es un ejemplo simplificado para ilustrar el funcionamiento del algoritmo. En los notebooks del repositorio encontrarás implementaciones más completas y análisis de resultados.*"
)
