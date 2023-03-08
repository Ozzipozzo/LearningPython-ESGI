{
    "_id": ObjectId('')
    "name": "string",
        "description": "string",
            "brand": "string",
                "category": "string",
                    "sub_category": "string",
                        "price": "number",
                            "stock": "number",
                                "image_url": "string",
                                    "attributes": {
        "color": "string",
            "size": "string",
                "weight": "string",
                    "material": "string"
    },
    "details": {
        "description": "string",
            "images": {
            "url": "string",
        }
    }
};

// Insérer une donnée produit
db.products.insertOne({
    name: "Raquette de Ping Pong",
    description: "Raquette de haute qualité avec un grip tenace",
    brand: "Adidas",
    category: "Sports",
    sub_category: "Tennis de table",
    price: 39.99,
    stock: 50,
    image_url: "https://www.example.com/images/table-tennis-paddle.jpg",
    attributes: {
        color: "Rouge",
        size: "unique",
        weight: "80g",
        material: "Fibre de carbon"
    },
    details: {
        description: "Raquette étudié avec des grands noms du tennis de table lorem ipsum",
        images: {
            url: "https://google.com"
        }
    }
});

// Récuperation de toutes les catégories
db.products.distinct("category", {});

// Récuperation de tous les  d'une catégorie sports
db.products.distinct("sub_category", {});

// Récuperation de tous les produits lié à un sport, vous pouvez remplacer le Running par un autre 
// sport
db.products.find({ "sub_category": "Running" });

// Récuperation d'une fiche produit d'un produit en particulier, à la place des x, il faut mettre un ObjectId("6407657b72360b1651c95526") d'un produit de mongodb
db.products.find({ _id: ObjectId("xxxxxxxxxxxxxxxx") }, { _id: 0, name: 1, description: 1, attributes: 1 });

// Rechercher un produit par son nom, par exemple ici "V"
db.products.find({ name: /^V/i })

// Rechercher un produit par son nom, et dans un range de prix
db.products.find({ name: /^V/i, price: { $gt: 50, $lt: 60 } })

// Rechercher un produit par son sport, et son prix
db.products.find({ sub_category: /^S/i, price: { $gt: 50, $lt: 60 } })

// ******* Aggregate ********** //
// trier tous les produits par ordre alphabétique
db.products.aggregate([{ $sort: {name: 1 }}])

// trier tous les produits par prix 1 pour le moins chère au plus chère et -1 pour le contraire
db.products.aggregate([{ $sort: { price: 1 } }])

// Trouver un produit par nom et filtrer du moins chère au plus chère
db.products.aggregate([
    { $match: { name: /^v/i } },
    { $sort: { price: 1 } }
])

// Trouver un produit par sport et filtrer du moins chère au plus chère
db.products.aggregate([
    { $match: { sub_category: /^v/i } },
    { $sort: { price: 1 } }
])

// trouver un produit via sa catégorie, son sport et trié par prix
db.products.aggregate([
  { $match: { category: /^v/i, sub_category: /^v/i } },
  { $sort: { price: 1 }}
])
