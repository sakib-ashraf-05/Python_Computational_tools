import pandas as pd


df = pd.read_csv("Q24/titanic.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


print("\nMissing Values:")
print(df.isnull().sum())


print("\nNumber of duplicates:", df.duplicated().sum())

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].median())

df["Fare"] = df["Fare"].fillna(df["Fare"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Name"] = df["Name"].fillna("Unknown")
df["Ticket"] = df["Ticket"].fillna("Unknown")

df["Cabin"] = df["Cabin"].fillna("Unknown")


df["Sex"] = df["Sex"].map({
    "male": 0,
    "female": 1
})

df["Embarked"] = df["Embarked"].map({
    "S": 0,
    "C": 1,
    "Q": 2
})


df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

df = df.drop(["Name", "Ticket", "Cabin"], axis=1)

print("\nCleaned Dataset:")
print(df.head())

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

df.to_csv("Q24/cleaned_titanic.csv", index=False)

print("\nCleaned dataset saved as cleaned_titanic.csv")