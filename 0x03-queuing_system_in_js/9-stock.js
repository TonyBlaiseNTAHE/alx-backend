const express = require('express');

const { app } = require('kue');

const redis = require('redis');

const listProducts = [
  { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 },
];

const getItemById = (id) => {
  return new Promise((resolve, reject) => {
    const item = listProducts.find((item) => item.id === id);
    if (item) {
      resolve(item);
    } else {
      reject(new Error('Item not found'));
    }
  });
}

express()
  .get('/list_products', (req, res) => {
    res.json(listProducts);
  })

  .get('/list_products/:id', (req, res) => {
    getItemById(req.params.id)
      .then((item) => res.json(item))
      .catch((error) => res.status(404).json({ error: error.message }));
  })

  .get('/reserve_product/:id', (req, res) => {
    getItemById(req.param.id)
    if (!item) {
      res.status(404).json({ error: 'Product not found' });
      express.then((item) => {
        if (item.stock > 0) {
          item.stock -= 1;
	  res.json({ status: 'Reservation confirmed', item });
	} else {
	  res.json({ status: 'Not enough stock available', item });
	}
      })
    }
  })

  app.listen(1245);

redis.createClient()
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (error) => console.log(`Redis client not connected to the server: ${error.message}`));

const reserveStockById = async (itemId, stock) => {
  return new Promise((resolve, reject) => {
    getItemById(itemId)
      .then((item) => {
        if (item.stock >= stock) {
          item.stock -= stock;
          resolve(item);
	} else {
          reject(new Error('Not enough stock available'));
	}
      })
      .catch((error) => reject(error));
  });
}

const getCurrentReservedStockById = async (itemId) => {
  return new Promise((resolve, reject) => {
    client.get(`item.${itemId}`, (error, stock) => {
      if (error) {
        reject(error);
      } else {
        resolve(stock);
      }
    });
  })
};
