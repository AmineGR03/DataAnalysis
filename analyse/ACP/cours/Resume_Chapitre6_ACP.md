# Résumé Complet - Chapitre 6 : Analyse en Composantes Principales (ACP)

## 1. DÉFINITION ET OBJECTIFS

### 1.1 Définition

L'**Analyse en Composantes Principales (ACP)** est :
- Une méthode descriptive multidimensionnelle
- Un outil statistique de **synthèse de l'information**
- Une méthode factorielle permettant d'analyser des tableaux de données quantitatives

### 1.2 Objectifs

L'ACP permet d'étudier :
1. **La variabilité entre les individus** : différences et ressemblances
2. **Les liaisons entre les variables** : groupes de variables corrélées, nouvelles variables synthétiques

### 1.3 Problème géométrique

- Le nuage de points des données s'inscrit dans un espace de **p dimensions**
- Chaque point représente un individu par rapport à \(x_1, x_2, ..., x_p\)
- Il est difficile de visualiser les relations dès que \(p > 3\)

**Solution** : Projeter le nuage sur des plans de dimension réduite (2D ou 3D) tout en conservant le maximum d'information.

---

## 2. NOTATIONS ET DÉFINITIONS

### 2.1 Matrice des données

Soit \(n\) individus caractérisés par \(p\) variables quantitatives. Les données sont présentées dans une **matrice des données** de dimension \(n \times p\) :

\[
\mathbf{X} = \begin{pmatrix}
x_{11} & x_{12} & \cdots & x_{1j} & \cdots & x_{1p} \\
x_{21} & x_{22} & \cdots & x_{2j} & \cdots & x_{2p} \\
\vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\
x_{i1} & x_{i2} & \cdots & x_{ij} & \cdots & x_{ip} \\
\vdots & \vdots & \ddots & \vdots & \ddots & \vdots \\
x_{n1} & x_{n2} & \cdots & x_{nj} & \cdots & x_{np}
\end{pmatrix}
\]

### 2.2 Individus et variables

- **Individu** \(e_i\) : vecteur de \(\mathbb{R}^p\) défini par \(e_i^\top = (x_{i1}, x_{i2}, ..., x_{ip})\)
- **Nuage des individus** : ensemble des vecteurs \(e_i, i = 1, ..., n\)
- **Variable** \(X_k\) : vecteur de \(\mathbb{R}^n\) défini par \(X_k^\top = (x_{1k}, x_{2k}, ..., x_{nk})\)
- **Nuage des variables** : ensemble des vecteurs \(X_k, k = 1, ..., p\)

### 2.3 Centre de gravité

Le vecteur individu moyen (centre de gravité) est :

\[
\mathbf{g}^\top = (\bar{x}_1, \bar{x}_2, ..., \bar{x}_p)
\]

où \(\bar{x}_j = \frac{1}{n}\sum_{i=1}^{n} x_{ij}\) est la moyenne de la variable \(X_j\).

---

## 3. CENTRAGE ET RÉDUCTION

### 3.1 Nécessité

Les \(p\) variables sont de nature différente. Pour **homogénéiser les unités**, les variables doivent être **centrées et réduites**.

### 3.2 Définition

Une variable est **centrée et réduite** si :
- Sa moyenne est nulle : \(\bar{X} = 0\)
- Sa variance est égale à 1 : \(Var(X) = 1\)

### 3.3 Matrice centrée réduite

La matrice centrée réduite \(\mathbf{M}_{cr} = (m_{ij})_{1 \leq i \leq n, 1 \leq j \leq p}\) est obtenue par :

\begin{align}
m_{ij} &= \frac{x_{ij} - \bar{x}_j}{\sigma_j} \\
\sigma_j &= \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_{ij} - \bar{x}_j)^2}
\end{align}

où :
- \(\bar{x}_j\) : moyenne de la variable \(X_j\)
- \(\sigma_j\) : écart-type de la variable \(X_j\)

### 3.4 Matrice centrée

La matrice centrée \(\mathbf{M}_c = (a_{ij})\) est obtenue par :

\[
a_{ij} = x_{ij} - \bar{x}_j
\]

---

## 4. MATRICES DE VARIANCE-COVARIANCE ET DE CORRÉLATION

### 4.1 Matrice des variances-covariances

#### Définition

\[
\mathbf{V} = \begin{pmatrix}
Var(X_1) & Cov(X_1, X_2) & \cdots & Cov(X_1, X_p) \\
Cov(X_2, X_1) & Var(X_2) & \cdots & Cov(X_2, X_p) \\
\vdots & \vdots & \ddots & \vdots \\
Cov(X_p, X_1) & Cov(X_p, X_2) & \cdots & Var(X_p)
\end{pmatrix}
\]

#### Calcul

\begin{align}
\mathbf{V} = \frac{1}{n} \mathbf{M}_c^T \mathbf{M}_c
\end{align}

où \(\mathbf{M}_c^T\) est la transposée de la matrice centrée.

#### Propriétés

- Si \(Cov(X_i, X_j) = 0\) : les variables \(X_i\) et \(X_j\) sont indépendantes (linéairement)
- Si \(Cov(X_i, X_j) \neq 0\) : les variables \(X_i\) et \(X_j\) sont dépendantes (relation linéaire)

### 4.2 Matrice des corrélations

#### Définition

La matrice des corrélations entre variables permet d'analyser les relations bilatérales entre les variables.

#### Calcul

\begin{align}
\mathbf{U} = \frac{1}{n} \mathbf{M}_{cr}^T \mathbf{M}_{cr}
\end{align}

où \(\mathbf{M}_{cr}^T\) est la transposée de la matrice centrée réduite.

#### Propriétés

- \(\mathbf{U}\) est une matrice symétrique
- Les éléments diagonaux valent 1 (corrélation d'une variable avec elle-même)
- Les éléments hors diagonale sont les coefficients de corrélation de Pearson entre variables

---

## 5. NOTION D'INERTIE

### 5.1 Définition

L'**inertie** du nuage des individus par rapport à son centre de gravité mesure la variabilité (dispersion) des données.

### 5.2 Calcul

\begin{align}
I_g = \frac{1}{n}\sum_{i=1}^{n}\sum_{k=1}^{p}(x_{ik} - \bar{x}_k)^2 = \sum_{k=1}^{p} \sigma_k^2
\end{align}

### 5.3 Cas des données centrées-réduites

Si les données sont centrées et réduites :
- \(I_g = p\)
- \(\mathbf{g}^\top = (0, 0, ..., 0)\)

**Dans la suite, on suppose que les données ont été centrées et réduites.**

---

## 6. DÉMARCHE DE L'ACP

### 6.1 Étapes principales

1. **Centrage et réduction** des données
2. **Déterminer les valeurs propres et vecteurs propres** de la matrice de corrélation \(\mathbf{U}\)
3. **Déterminer les axes factoriels**
4. **Sélectionner les composantes principales**

---

## 7. VALEURS PROPRES ET VECTEURS PROPRES

### 7.1 Polynôme caractéristique

Pour trouver les valeurs propres de \(\mathbf{U}\), on résout :

\begin{align}
P(\lambda) = \det(\mathbf{U} - \lambda \mathbf{I}_p) = 0
\end{align}

où \(\mathbf{I}_p\) est la matrice identité de dimension \(p \times p\).

### 7.2 Valeurs propres

Les valeurs propres \(\lambda_1, \lambda_2, ..., \lambda_p\) sont ordonnées par ordre décroissant :

\begin{align}
\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_p \geq 0
\end{align}

### 7.3 Vecteurs propres

Pour chaque valeur propre \(\lambda_k\), on trouve le vecteur propre associé \(\mathbf{u}_k\) tel que :

\begin{align}
\mathbf{U}\mathbf{u}_k = \lambda_k \mathbf{u}_k
\end{align}

Les vecteurs propres sont **orthonormés** (orthogonaux et de norme 1).

---

## 8. AXES FACTORIELS ET COMPOSANTES PRINCIPALES

### 8.1 Axes principaux d'inertie

Les **axes principaux d'inertie** sont les axes de direction des vecteurs propres de \(\mathbf{U}\) normés à 1.

- **Axe 1** : associé à la plus grande valeur propre \(\lambda_1\), noté \(\mathbf{u}_1\)
- **Axe 2** : associé à la deuxième valeur propre \(\lambda_2\), noté \(\mathbf{u}_2\)
- ...
- **Axe p** : associé à la valeur propre \(\lambda_p\), noté \(\mathbf{u}_p\)

### 8.2 Composantes principales

À chaque axe est associée une variable appelée **composante principale**.

- **Composante \(C_1\)** : vecteur contenant les coordonnées des projections des individus sur l'axe 1
- **Composante \(C_2\)** : vecteur contenant les coordonnées des projections des individus sur l'axe 2
- ...

#### Calcul

\begin{align}
\mathbf{C}_1 &= \mathbf{M}_{cr} \mathbf{u}_1 \\
\mathbf{C}_2 &= \mathbf{M}_{cr} \mathbf{u}_2 \\
&\vdots \\
\mathbf{C}_k &= \mathbf{M}_{cr} \mathbf{u}_k
\end{align}

### 8.3 Propriétés des composantes principales

1. **Centrées** : la moyenne de chaque composante est nulle
2. **Variance** : la variance de la composante \(C_k\) est égale à la valeur propre \(\lambda_k\)
3. **Non corrélées** : les composantes principales sont deux à deux non corrélées

---

## 9. INERTIE EXPLIQUÉE

### 9.1 Définition

L'**inertie expliquée** par un axe principal mesure la quantité d'information contenue dans cet axe.

### 9.2 Calcul

\begin{align}
\text{Inertie axe } k = \frac{\lambda_k}{\sum_{i=1}^{p} \lambda_i} = \frac{\lambda_k}{I_g}
\end{align}

Pour des données centrées-réduites, \(I_g = p\), donc :

\begin{align}
\text{Inertie axe } k = \frac{\lambda_k}{p}
\end{align}

### 9.3 Inertie cumulée

L'inertie cumulée des \(k\) premiers axes est :

\begin{align}
\text{Inertie cumulée} = \frac{\sum_{i=1}^{k} \lambda_i}{\sum_{i=1}^{p} \lambda_i}
\end{align}

### 9.4 Interprétation

- Plus l'inertie expliquée est élevée, plus l'axe contient d'information
- On retient généralement les axes qui expliquent au moins 70-80% de l'inertie totale

---

## 10. CONTRIBUTIONS

### 10.1 Contribution des individus à l'inertie

La contribution de l'individu \(i\) à l'inertie totale est :

\begin{align}
\text{CONTR}(i) = \frac{1}{n} \sum_{j=1}^{p} \frac{m_{ij}^2}{I_g}
\end{align}

où \(m_{ij}\) est l'élément de la matrice centrée réduite \(\mathbf{M}_{cr}\).

Pour des données centrées-réduites (\(I_g = p\)) :

\begin{align}
\text{CONTR}(i) = \frac{1}{np} \sum_{j=1}^{p} m_{ij}^2
\end{align}

### 10.2 Contribution des variables

La contribution de la variable \(X_j\) à l'inertie totale est :

\begin{align}
\text{CONTR}(X_j) = \frac{1}{p} \sum_{i=1}^{n} \frac{m_{ij}^2}{I_g}
\end{align}

### 10.3 Contribution des individus à la construction des axes

La contribution de l'individu \(i\) à la construction de l'axe \(k\) est :

\begin{align}
\text{CONTR}(i, \text{axe } k) = \frac{1}{n} \frac{C_{ik}^2}{\lambda_k}
\end{align}

où \(C_{ik}\) est la coordonnée de l'individu \(i\) sur la composante principale \(C_k\).

---

## 11. RÉSUMÉ DES FORMULES CLÉS

### Matrices

| Matrice | Formule |
|---------|---------|
| Centrée | \(a_{ij} = x_{ij} - \bar{x}_j\) |
| Centrée réduite | \(m_{ij} = \frac{x_{ij} - \bar{x}_j}{\sigma_j}\) |
| Variances-covariances | \(\mathbf{V} = \frac{1}{n}\mathbf{M}_c^T\mathbf{M}_c\) |
| Corrélations | \(\mathbf{U} = \frac{1}{n}\mathbf{M}_{cr}^T\mathbf{M}_{cr}\) |

### Valeurs et vecteurs propres

\begin{align}
\mathbf{U}\mathbf{u}_k = \lambda_k \mathbf{u}_k, \quad k = 1, ..., p
\end{align}

### Composantes principales

\begin{align}
\mathbf{C}_k = \mathbf{M}_{cr} \mathbf{u}_k
\end{align}

### Inertie

| Concept | Formule |
|---------|---------|
| Inertie totale | \(I_g = \sum_{k=1}^{p} \sigma_k^2 = p\) (si centré-réduit) |
| Inertie axe \(k\) | \(\frac{\lambda_k}{\sum_{i=1}^{p} \lambda_i}\) |
| Inertie cumulée | \(\frac{\sum_{i=1}^{k} \lambda_i}{\sum_{i=1}^{p} \lambda_i}\) |

### Contributions

| Type | Formule |
|------|---------|
| Individu \(i\) | \(\text{CONTR}(i) = \frac{1}{np}\sum_{j=1}^{p} m_{ij}^2\) |
| Variable \(X_j\) | \(\text{CONTR}(X_j) = \frac{1}{p}\sum_{i=1}^{n} \frac{m_{ij}^2}{I_g}\) |
| Individu \(i\) à l'axe \(k\) | \(\text{CONTR}(i, \text{axe } k) = \frac{1}{n}\frac{C_{ik}^2}{\lambda_k}\) |

---

## 12. OPÉRATIONS SUR MATRICES (Rappels)

### 12.1 Multiplication matricielle

Pour \(\mathbf{A}\) (m×n) et \(\mathbf{B}\) (n×p) :

\[
(\mathbf{AB})_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}
\]

### 12.2 Transposée

\[
(\mathbf{A}^T)_{ij} = a_{ji}
\]

### 12.3 Propriétés importantes

- \((\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T\)
- \((\mathbf{A}^T)^T = \mathbf{A}\)
- Si \(\mathbf{A}\) est symétrique : \(\mathbf{A}^T = \mathbf{A}\)

### 12.4 Déterminant

Pour une matrice carrée \(\mathbf{A}\) (2×2) :

\[
\det(\mathbf{A}) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc
\]

Pour une matrice (3×3) :

\[
\det(\mathbf{A}) = a(ei - fh) - b(di - fg) + c(dh - eg)
\]

---

## 13. EXERCICE D'APPLICATION

### Énoncé

Une étude porte sur 4 pays (A, B, C, D) caractérisés par 3 variables économiques :
- \(X_1\) : Investissements directs étrangers (IDE) en millions d'euros
- \(X_2\) : Taux de croissance économique (%)
- \(X_3\) : Taux d'inflation (%)

**Tableau des données** :

| Pays | IDE (\(X_1\)) | Taux croissance (\(X_2\)) | Taux inflation (\(X_3\)) |
|------|--------------|--------------------------|------------------------|
| A    | 300          | 2                        | 6                       |
| B    | 450          | 2                        | 4                       |
| C    | 950          | 8                        | 2                       |
| D    | 700          | 7                        | 5                       |

**Travail à faire** :

1. Calculer la moyenne et l'écart-type de chaque variable.
2. Déterminer la matrice centrée réduite \(\mathbf{M}_{cr}\).
3. Déterminer la matrice des variances-covariances \(\mathbf{V}\).
4. Déterminer la matrice des corrélations \(\mathbf{U}\).
5. Calculer les valeurs propres de \(\mathbf{U}\).
6. Calculer et interpréter l'inertie expliquée des axes factoriels.
7. Déterminer les vecteurs propres orthogonaux associés aux valeurs propres.
8. Calculer les composantes principales.
9. Calculer la contribution des individus et des variables.
10. Calculer la contribution des individus à la construction des axes.

### Solution guidée

#### 1. Moyennes et écarts-types

**Moyennes** :

\[
\bar{x}_1 = \frac{300 + 450 + 950 + 700}{4} = \frac{2400}{4} = 600
\]

\[
\bar{x}_2 = \frac{2 + 2 + 8 + 7}{4} = \frac{19}{4} = 4.75
\]

\[
\bar{x}_3 = \frac{6 + 4 + 2 + 5}{4} = \frac{17}{4} = 4.25
\]

**Écarts-types** :

\[
\sigma_1 = \sqrt{\frac{1}{4}[(300-600)^2 + (450-600)^2 + (950-600)^2 + (700-600)^2]}
\]

\[
= \sqrt{\frac{1}{4}[90000 + 22500 + 122500 + 10000]} = \sqrt{61250} \approx 247.49
\]

\[
\sigma_2 = \sqrt{\frac{1}{4}[(2-4.75)^2 + (2-4.75)^2 + (8-4.75)^2 + (7-4.75)^2]}
\]

\[
= \sqrt{\frac{1}{4}[7.5625 + 7.5625 + 10.5625 + 5.0625]} = \sqrt{7.6875} \approx 2.77
\]

\[
\sigma_3 = \sqrt{\frac{1}{4}[(6-4.25)^2 + (4-4.25)^2 + (2-4.25)^2 + (5-4.25)^2]}
\]

\[
= \sqrt{\frac{1}{4}[3.0625 + 0.0625 + 5.0625 + 0.5625]} = \sqrt{2.1875} \approx 1.48
\]

#### 2. Matrice centrée réduite

\[
m_{ij} = \frac{x_{ij} - \bar{x}_j}{\sigma_j}
\]

\[
\mathbf{M}_{cr} = \begin{pmatrix}
\frac{300-600}{247.49} & \frac{2-4.75}{2.77} & \frac{6-4.25}{1.48} \\
\frac{450-600}{247.49} & \frac{2-4.75}{2.77} & \frac{4-4.25}{1.48} \\
\frac{950-600}{247.49} & \frac{8-4.75}{2.77} & \frac{2-4.25}{1.48} \\
\frac{700-600}{247.49} & \frac{7-4.75}{2.77} & \frac{5-4.25}{1.48}
\end{pmatrix}
= \begin{pmatrix}
-1.21 & -0.99 & 1.18 \\
-0.61 & -0.99 & -0.17 \\
1.41 & 1.17 & -1.52 \\
0.40 & 0.81 & 0.51
\end{pmatrix}
\]

#### 3. Matrice des variances-covariances

D'abord, la matrice centrée :

\[
\mathbf{M}_c = \begin{pmatrix}
-300 & -2.75 & 1.75 \\
-150 & -2.75 & -0.25 \\
350 & 3.25 & -2.25 \\
100 & 2.25 & 0.75
\end{pmatrix}
\]

\[
\mathbf{V} = \frac{1}{4} \mathbf{M}_c^T \mathbf{M}_c = \begin{pmatrix}
61250 & 650 & -300 \\
650 & 7.6875 & -2.4375 \\
-300 & -2.4375 & 2.1875
\end{pmatrix}
\]

#### 4. Matrice des corrélations

\[
\mathbf{U} = \frac{1}{4} \mathbf{M}_{cr}^T \mathbf{M}_{cr} = \begin{pmatrix}
1 & 0.95 & -0.82 \\
0.95 & 1 & -0.6 \\
-0.82 & -0.6 & 1
\end{pmatrix}
\]

**Interprétation** :
- \(r(X_1, X_2) = 0.95\) : Forte corrélation positive entre IDE et taux de croissance
- \(r(X_1, X_3) = -0.82\) : Forte corrélation négative entre IDE et taux d'inflation
- \(r(X_2, X_3) = -0.6\) : Corrélation négative modérée entre taux de croissance et taux d'inflation

#### 5. Valeurs propres

Le polynôme caractéristique est :

\[
P(\lambda) = \det(\mathbf{U} - \lambda \mathbf{I}_3) = 0
\]

En résolvant, on trouve :

\[
\lambda_1 = 2.57, \quad \lambda_2 = 0.43, \quad \lambda_3 = 0
\]

(On ignore \(\lambda_3 = 0\) car il n'apporte pas d'information)

#### 6. Inertie expliquée

**Inertie totale** : \(I_g = 3\) (car 3 variables centrées-réduites)

**Axe 1** :

\[
\text{Inertie axe 1} = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{2.57}{2.57 + 0.43} = \frac{2.57}{3} = 0.857 \text{ (85.7%)}
\]

**Axe 2** :

\[
\text{Inertie axe 2} = \frac{\lambda_2}{\lambda_1 + \lambda_2} = \frac{0.43}{3} = 0.143 \text{ (14.3%)}
\]

**Interprétation** : L'axe 1 contient **85.7%** de l'information, l'axe 2 en contient **14.3%**. Les deux premiers axes expliquent **100%** de l'information (car \(\lambda_3 = 0\)).

#### 7. Vecteurs propres

**Axe 1** (\(\lambda_1 = 2.57\)) :

En résolvant \(\mathbf{U}\mathbf{u}_1 = 2.57\mathbf{u}_1\), on trouve :

\[
\mathbf{u}_1 = \begin{pmatrix} -0.62 \\ -0.57 \\ -0.54 \end{pmatrix}
\]

**Axe 2** (\(\lambda_2 = 0.43\)) :

En résolvant \(\mathbf{U}\mathbf{u}_2 = 0.43\mathbf{u}_2\), on trouve :

\[
\mathbf{u}_2 = \begin{pmatrix} 0.12 \\ 0.61 \\ 0.79 \end{pmatrix}
\]

#### 8. Composantes principales

\[
\mathbf{C}_1 = \mathbf{M}_{cr} \mathbf{u}_1 = \begin{pmatrix}
-1.21 & -0.99 & 1.18 \\
-0.61 & -0.99 & -0.17 \\
1.41 & 1.17 & -1.52 \\
0.40 & 0.81 & 0.51
\end{pmatrix} \begin{pmatrix} -0.62 \\ -0.57 \\ -0.54 \end{pmatrix}
= \begin{pmatrix} 0.68 \\ 1.03 \\ -0.72 \\ -0.99 \end{pmatrix}
\]

\[
\mathbf{C}_2 = \mathbf{M}_{cr} \mathbf{u}_2 = \begin{pmatrix}
-1.21 & -0.99 & 1.18 \\
-0.61 & -0.99 & -0.17 \\
1.41 & 1.17 & -1.52 \\
0.40 & 0.81 & 0.51
\end{pmatrix} \begin{pmatrix} 0.12 \\ 0.61 \\ 0.79 \end{pmatrix}
= \begin{pmatrix} 0.18 \\ -0.81 \\ -0.32 \\ 0.94 \end{pmatrix}
\]

**Tableau des composantes principales** :

| Pays | \(C_1\) | \(C_2\) |
|------|---------|--------|
| A    | 0.68    | 0.18   |
| B    | 1.03    | -0.81  |
| C    | -0.72   | -0.32  |
| D    | -0.99   | 0.94   |

#### 9. Contribution des individus et variables

**Contribution des individus** :

\[
\text{CONTR}(i) = \frac{1}{np}\sum_{j=1}^{p} m_{ij}^2 = \frac{1}{4 \times 3}\sum_{j=1}^{3} m_{ij}^2
\]

- Pays A : \(\text{CONTR}(A) = \frac{1}{12}[(-1.21)^2 + (-0.99)^2 + (1.18)^2] = \frac{1}{12}[1.464 + 0.980 + 1.392] = 0.32\)
- Pays B : \(\text{CONTR}(B) = \frac{1}{12}[(-0.61)^2 + (-0.99)^2 + (-0.17)^2] = 0.11\)
- Pays C : \(\text{CONTR}(C) = \frac{1}{12}[(1.41)^2 + (1.17)^2 + (-1.52)^2] = 0.47\)
- Pays D : \(\text{CONTR}(D) = \frac{1}{12}[(0.40)^2 + (0.81)^2 + (0.51)^2] = 0.17\)

**Interprétation** : Le pays C contribue le plus (47%) à l'analyse.

**Contribution des variables** :

\[
\text{CONTR}(X_j) = \frac{1}{p}\sum_{i=1}^{n} \frac{m_{ij}^2}{I_g} = \frac{1}{3}\sum_{i=1}^{4} \frac{m_{ij}^2}{3}
\]

- \(X_1\) : \(\text{CONTR}(X_1) = \frac{1}{9}[(1.21)^2 + (0.61)^2 + (1.41)^2 + (0.40)^2] = 0.42\)
- \(X_2\) : \(\text{CONTR}(X_2) = \frac{1}{9}[(0.99)^2 + (0.99)^2 + (1.17)^2 + (0.81)^2] = 0.32\)
- \(X_3\) : \(\text{CONTR}(X_3) = \frac{1}{9}[(1.18)^2 + (0.17)^2 + (1.52)^2 + (0.51)^2] = 0.33\)

**Interprétation** : La variable IDE (\(X_1\)) contribue le plus (42%) à l'analyse.

#### 10. Contribution des individus aux axes

**Axe 1** :

\[
\text{CONTR}(i, \text{axe } 1) = \frac{1}{n}\frac{C_{i1}^2}{\lambda_1} = \frac{1}{4}\frac{C_{i1}^2}{2.57}
\]

- Pays A : \(\text{CONTR}(A, \text{axe } 1) = \frac{1}{4} \times \frac{(0.68)^2}{2.57} = 0.04\)
- Pays B : \(\text{CONTR}(B, \text{axe } 1) = \frac{1}{4} \times \frac{(1.03)^2}{2.57} = 0.10\)
- Pays C : \(\text{CONTR}(C, \text{axe } 1) = \frac{1}{4} \times \frac{(-0.72)^2}{2.57} = 0.05\)
- Pays D : \(\text{CONTR}(D, \text{axe } 1) = \frac{1}{4} \times \frac{(-0.99)^2}{2.57} = 0.09\)

**Axe 2** :

\[
\text{CONTR}(i, \text{axe } 2) = \frac{1}{n}\frac{C_{i2}^2}{\lambda_2} = \frac{1}{4}\frac{C_{i2}^2}{0.43}
\]

- Pays A : \(\text{CONTR}(A, \text{axe } 2) = \frac{1}{4} \times \frac{(0.18)^2}{0.43} = 0.02\)
- Pays B : \(\text{CONTR}(B, \text{axe } 2) = \frac{1}{4} \times \frac{(-0.81)^2}{0.43} = 0.38\)
- Pays C : \(\text{CONTR}(C, \text{axe } 2) = \frac{1}{4} \times \frac{(-0.32)^2}{0.43} = 0.06\)
- Pays D : \(\text{CONTR}(D, \text{axe } 2) = \frac{1}{4} \times \frac{(0.94)^2}{0.43} = 0.51\)

**Interprétation** :
- Pour l'axe 1 : Le pays B contribue le plus (10%)
- Pour l'axe 2 : Le pays D contribue le plus (51%)

---

## 14. INTERPRÉTATION DES RÉSULTATS

### 14.1 Plan factoriel

En projetant les individus sur le plan formé par les axes 1 et 2, on peut visualiser :
- Les **similarités** entre pays (proximité des points)
- Les **oppositions** (points éloignés)
- Les **groupes** de pays

### 14.2 Variables et axes

Les coordonnées des variables sur les axes permettent d'interpréter :
- Quelles variables contribuent le plus à chaque axe
- Les relations entre variables

### 14.3 Critères de sélection des axes

On retient généralement les axes qui :
- Expliquent au moins 70-80% de l'inertie totale
- Ont une inertie expliquée > 1/p (règle de Kaiser)
- Permettent une interprétation claire

---

## 15. RÉSUMÉ FINAL

L'ACP est une méthode puissante pour :
- **Réduire la dimension** des données
- **Visualiser** les relations entre individus et variables
- **Synthétiser** l'information contenue dans un tableau de données
- **Identifier** des groupes et des oppositions

Les étapes clés sont :
1. Centrer et réduire les données
2. Calculer la matrice de corrélation
3. Extraire valeurs et vecteurs propres
4. Calculer les composantes principales
5. Interpréter les résultats

