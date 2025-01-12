const express = require('express');
const router = express.Router();
const quranData = require('../data/merged_surah_data.json');

// Search API
router.get('/', (req, res) => {
    const query = req.query.q?.toLowerCase();
    if (!query) return res.status(400).json({ message: 'Query parameter is required' });

    const results = [];
    quranData.forEach((chapter) => {
        chapter.forEach((ayah) => {
            if (ayah.tafsir_text.toLowerCase().includes(query)) {
                results.push({
                    tafsir_text: ayah.tafsir_text,
                    text: ayah.text
                });
            }
        });
    });

    res.json({ results });
});

module.exports = router;
