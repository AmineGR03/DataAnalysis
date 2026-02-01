# Résumé Complet - Chapitre 3 : Corrélation et Régression

## 1. CORRÉLATION ET COEFFICIENT DE CORRÉLATION DE PEARSON

### 1.1 Définitions

**Relation entre deux variables** : Lien ou dépendance entre deux variables quantitatives.

**Types de relations** :
- Relation linéaire (droite)
- Relation non linéaire (courbe, parabole)
- Absence de relation (données dispersées)

**Corrélation** : Mesure statistique qui exprime la force et la direction de la relation entre deux variables quantitatives.

⚠️ **Important** : Corrélation ≠ Causalité !

### 1.2 Types de corrélation

- **Positive** : Les deux variables augmentent ensemble
- **Négative** : Une variable augmente, l'autre diminue
- **Nulle** : Absence de relation linéaire

### 1.3 Coefficient de corrélation de Pearson

#### Formule principale

\begin{align}
r = \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n}(x_i - \bar{x})^2 \sum_{i=1}^{n}(y_i - \bar{y})^2}}
\end{align}

où :
- \(x_i, y_i\) : valeurs observées
- \(\bar{x}, \bar{y}\) : moyennes des variables X et Y
- \(n\) : nombre d'observations

#### Propriétés

- \(-1 \leq r \leq 1\)
- \(r = 1\) : corrélation positive parfaite
- \(r = -1\) : corrélation négative parfaite
- \(r = 0\) : absence de corrélation linéaire

#### Interprétation de r

| Valeur de |r| | Interprétation |
|----------|---|----------------|
| 0.9 ≤ |r| ≤ 1 | Très forte corrélation |
| 0.7 ≤ |r| < 0.9 | Forte corrélation |
| 0.5 ≤ |r| < 0.7 | Corrélation modérée |
| 0.3 ≤ |r| < 0.5 | Faible corrélation |
| 0 ≤ |r| < 0.3 | Très faible ou aucune corrélation |

### 1.4 Précautions

- Corrélation ≠ causalité
- Présence de valeurs extrêmes (outliers) → influence sur r
- Relation non linéaire non détectée par Pearson
- Toujours visualiser les données

### 1.5 Autres coefficients de corrélation

- **Spearman** : pour données ordinales ou non linéaires
- **Kendall** : pour petites séries ordinales
- **Pearson** : uniquement pour relation linéaire et données quantitatives

---

## 2. RÉGRESSION LINÉAIRE SIMPLE

### 2.1 Définition

**Régression linéaire simple** : Méthode statistique permettant de modéliser la relation entre une variable expliquée (réponse) Y et une variable explicative (prédicteur) X via une relation linéaire.

#### Modèle mathématique

\[
Y = \beta_0 + \beta_1 X + \varepsilon
\]

où :
- \(\beta_0\) : ordonnée à l'origine (intercept)
- \(\beta_1\) : coefficient directeur (pente)
- \(\varepsilon\) : erreur aléatoire

### 2.2 Hypothèses du modèle

1. Relation linéaire entre X et Y
2. Espérance nulle des erreurs : \(E[\varepsilon] = 0\)
3. Variance constante des erreurs : homoscédasticité
4. Indépendance des erreurs
5. Normalité des erreurs (optionnelle pour estimation, nécessaire pour les tests)

### 2.3 Estimation des paramètres par moindres carrés

#### Objectif

Minimiser la somme des carrés des erreurs :

\[
S(\beta_0, \beta_1) = \sum_{i=1}^{n}(y_i - \beta_0 - \beta_1 x_i)^2
\]

#### Solutions (estimateurs)

\begin{align}
\hat{\beta}_1 &= \frac{\sum_{i=1}^{n}(x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n}(x_i - \bar{x})^2} \\
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1\bar{x}
\end{align}

#### Équation estimée

\[
\hat{Y} = \hat{\beta_0} + \hat{\beta_1}X
\]

### 2.4 Coefficient de détermination R²

#### Définition

\begin{align}
R^2 = \frac{SS_{\text{exp}}}{SS_{\text{tot}}} = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\end{align}

où :
- \(SS_{\text{tot}} = \sum_{i=1}^{n}(y_i - \bar{y})^2\) : variabilité totale
- \(SS_{\text{res}} = \sum_{i=1}^{n}(y_i - \hat{y}_i)^2\) : variabilité non expliquée (résiduelle)
- \(SS_{\text{exp}} = \sum_{i=1}^{n}(\hat{y}_i - \bar{y})^2\) : variabilité expliquée

#### Interprétation de R²

| R² | Interprétation |
|----|----------------|
| 1 | Le modèle explique parfaitement les données |
| 0 | Le modèle n'explique aucune variance |
| 0 < R² < 1 | Le modèle explique partiellement la variance |

Plus R² est proche de 1, plus le modèle est performant.

### 2.5 Résidus

#### Définition

Un résidu est la différence entre la valeur observée et la valeur prédite :

\begin{align}
e_i = y_i - \hat{y}_i
\end{align}

#### Rôle des résidus

- Évaluer la qualité de l'ajustement
- Identifier les valeurs aberrantes
- Vérifier les hypothèses (linéarité, homoscédasticité, indépendance, normalité)

---

## 3. RÉGRESSION LINÉAIRE MULTIPLE

### 3.1 Définition

**Régression linéaire multiple** : Modélisation d'une variable réponse Y en fonction de plusieurs variables explicatives \(X_1, X_2, ..., X_p\).

#### Modèle mathématique

\[
Y_i = \beta_0 + \beta_1 X_{i1} + \beta_2 X_{i2} + \cdots + \beta_p X_{ip} + \varepsilon_i
\]

#### Notation matricielle

\[
\mathbf{Y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}
\]

où :
- \(\mathbf{Y}\) : vecteur des observations (n×1)
- \(\mathbf{X}\) : matrice des données (n×(p+1)), première colonne = 1 pour l'intercept
- \(\boldsymbol{\beta}\) : vecteur des coefficients de régression ((p+1)×1)
- \(\boldsymbol{\varepsilon}\) : vecteur des erreurs aléatoires (n×1)

### 3.2 Hypothèses du modèle

1. **Linéarité** : relation linéaire entre chaque \(X_j\) et Y
2. **Espérance nulle** : \(E[\varepsilon_i] = 0\)
3. **Homoscédasticité** : \(Var(\varepsilon_i) = \sigma^2\) (constante)
4. **Indépendance** : les erreurs sont indépendantes
5. **Normalité** : \(\varepsilon_i \sim N(0, \sigma^2)\) (pour les tests)

### 3.3 Estimation par moindres carrés ordinaires (MCO)

#### Objectif

Minimiser : \(\min_{\boldsymbol{\beta}} \|\mathbf{Y} - \mathbf{X}\boldsymbol{\beta}\|^2\)

#### Solution

\begin{align}
\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
\end{align}

⚠️ **Condition** : \((\mathbf{X}^T\mathbf{X})\) doit être inversible (pas de colinéarité parfaite).

### 3.4 Interprétation des coefficients

- \(\hat{\beta_j}\) : variation moyenne de Y lorsque \(X_j\) augmente d'une unité, toutes les autres variables étant maintenues constantes
- \(\hat{\beta_0}\) : valeur prédite de Y lorsque toutes les variables explicatives valent 0 (intercept)

### 3.5 Qualité de l'ajustement

#### R² (coefficient de détermination)

\begin{align}
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\end{align}

#### R² ajusté

\begin{align}
R^2_{\text{ajusté}} = 1 - (n-1)\frac{1-R^2}{n-p-1}
\end{align}

où :
- \(n\) : nombre d'observations
- \(p\) : nombre de variables explicatives

**Remarque** : \(R^2_{ajusté} \leq R^2\)

Le R² ajusté pénalise l'ajout de variables non pertinentes.

---

## 4. OPÉRATIONS SUR MATRICES (Rappels)

### 4.1 Multiplication matricielle

Pour \(\mathbf{A}\) (m×n) et \(\mathbf{B}\) (n×p) :

\[
(\mathbf{AB})_{ij} = \sum_{k=1}^{n} a_{ik}b_{kj}
\]

### 4.2 Transposée

\[
(\mathbf{A}^T)_{ij} = a_{ji}
\]

### 4.3 Inverse

\[
\mathbf{A}^{-1}\mathbf{A} = \mathbf{A}\mathbf{A}^{-1} = \mathbf{I}
\]

où \(\mathbf{I}\) est la matrice identité.

### 4.4 Propriétés importantes

- \((\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T\)
- \((\mathbf{A}^T)^T = \mathbf{A}\)
- \((\mathbf{A}^{-1})^T = (\mathbf{A}^T)^{-1}\)
- \((\mathbf{AB})^{-1} = \mathbf{B}^{-1}\mathbf{A}^{-1}\) (si les inverses existent)

---

## 5. EXERCICE D'APPLICATION

### Énoncé

Un chercheur étudie la relation entre le nombre d'heures d'étude par semaine (X) et la note obtenue à un examen (Y sur 20). Les données suivantes ont été collectées :

| Étudiant | Heures d'étude (X) | Note (Y) |
|----------|-------------------|----------|
| 1        | 5                 | 10       |
| 2        | 8                 | 12       |
| 3        | 10                | 15       |
| 4        | 12                | 16       |
| 5        | 15                | 18       |
| 6        | 18                | 19       |
| 7        | 20                | 20       |

**Questions** :

1. **Calculer le coefficient de corrélation de Pearson** entre X et Y. Interpréter le résultat.

2. **Estimer les paramètres** \(\beta_0\) et \(\beta_1\) du modèle de régression linéaire simple \(Y = \beta_0 + \beta_1 X + \varepsilon\).

3. **Calculer le coefficient de détermination R²** et interpréter.

4. **Prédire la note** d'un étudiant qui étudie 14 heures par semaine.

5. **Calculer les résidus** pour chaque observation et vérifier s'il y a des valeurs aberrantes.

### Solution guidée

#### 1. Calcul du coefficient de corrélation

**Étape 1** : Calculer les moyennes
- \(\bar{x} = \frac{5+8+10+12+15+18+20}{7} = 12.57\)
- \(\bar{y} = \frac{10+12+15+16+18+19+20}{7} = 15.71\)

**Étape 2** : Calculer les écarts et produits croisés

| i | \(x_i - \bar{x}\) | \(y_i - \bar{y}\) | \((x_i - \bar{x})(y_i - \bar{y})\) | \((x_i - \bar{x})^2\) | \((y_i - \bar{y})^2\) |
|---|-------------------|-------------------|-----------------------------------|----------------------|----------------------|
| 1 | -7.57             | -5.71             | 43.20                             | 57.30                | 32.60                |
| 2 | -4.57             | -3.71             | 16.96                             | 20.90                | 13.76                |
| 3 | -2.57             | -0.71             | 1.82                              | 6.60                 | 0.50                 |
| 4 | -0.57             | 0.29              | -0.17                             | 0.33                 | 0.08                 |
| 5 | 2.43              | 2.29              | 5.56                              | 5.90                 | 5.24                 |
| 6 | 5.43              | 3.29              | 17.87                             | 29.48                | 10.82                |
| 7 | 7.43              | 4.29              | 31.87                             | 55.20                | 18.40                |
| **Total** | | | **117.11** | **175.71** | **81.40** |

**Étape 3** : Calculer r

\[
r = \frac{117.11}{\sqrt{175.71 \times 81.40}} = \frac{117.11}{119.58} = 0.979
\]

**Interprétation** : \(r = 0.979\) indique une **très forte corrélation positive** entre le nombre d'heures d'étude et la note obtenue.

#### 2. Estimation des paramètres

\[
\hat{\beta_1} = \frac{117.11}{175.71} = 0.666
\]

\[
\hat{\beta_0} = 15.71 - 0.666 \times 12.57 = 7.34
\]

**Équation estimée** : \(\hat{Y} = 7.34 + 0.666X\)

#### 3. Calcul de R²

**Étape 1** : Calculer les valeurs prédites \(\hat{y_i}\)

| i | \(x_i\) | \(y_i\) | \(\hat{y_i} = 7.34 + 0.666x_i\) | \((y_i - \bar{y})^2\) | \((\hat{y_i} - \bar{y})^2\) | \((y_i - \hat{y_i})^2\) |
|---|---------|---------|--------------------------------|----------------------|---------------------------|------------------------|
| 1 | 5       | 10      | 10.67                           | 32.60                | 25.40                     | 0.45                   |
| 2 | 8       | 12      | 12.67                           | 13.76                | 9.24                      | 0.45                   |
| 3 | 10      | 15      | 14.00                           | 0.50                 | 2.92                      | 1.00                   |
| 4 | 12      | 16      | 15.33                           | 0.08                 | 0.14                      | 0.45                   |
| 5 | 15      | 18      | 17.33                           | 5.24                 | 2.63                      | 0.45                   |
| 6 | 18      | 19      | 19.33                           | 10.82                | 13.11                     | 0.11                   |
| 7 | 20      | 20      | 20.66                           | 18.40                | 24.50                     | 0.44                   |
| **Total** | | | | **81.40** | **76.98** | **3.35** |

**Étape 2** : Calculer R²

\[
R^2 = \frac{76.98}{81.40} = 0.946
\]

**Interprétation** : Le modèle explique **94.6%** de la variance des notes. C'est un excellent ajustement.

#### 4. Prédiction

Pour \(X = 14\) heures :

\[
\hat{Y} = 7.34 + 0.666 \times 14 = 16.66
\]

**Prédiction** : Un étudiant qui étudie 14 heures par semaine devrait obtenir environ **16.66/20**.

#### 5. Résidus

| i | \(y_i\) | \(\hat{y_i}\) | \(e_i = y_i - \hat{y_i}\) |
|---|---------|---------------|---------------------------|
| 1 | 10      | 10.67         | -0.67                     |
| 2 | 12      | 12.67         | -0.67                     |
| 3 | 15      | 14.00         | 1.00                      |
| 4 | 16      | 15.33         | 0.67                      |
| 5 | 18      | 17.33         | 0.67                      |
| 6 | 19      | 19.33         | -0.33                     |
| 7 | 20      | 20.66         | -0.66                     |

Tous les résidus sont petits (inférieurs à 1 en valeur absolue), donc **pas de valeurs aberrantes** détectées.

---

## 6. RÉSUMÉ DES FORMULES CLÉS

### Corrélation
\[
r = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum(x_i - \bar{x})^2 \sum(y_i - \bar{y})^2}}
\]

### Régression simple
\begin{align}
\hat{\beta}_1 &= \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2} \\
\hat{\beta}_0 &= \bar{y} - \hat{\beta}_1\bar{x}
\end{align}

### Régression multiple (matricielle)
\[
\hat{\boldsymbol{\beta}} = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{Y}
\]

### R²
\begin{align}
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\end{align}

### Résidus
\begin{align}
e_i = y_i - \hat{y}_i
\end{align}

