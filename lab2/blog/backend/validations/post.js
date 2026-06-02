import { body } from 'express-validator';

export const postCreateValidation = [
    body('title')
        .notEmpty()
        .withMessage("Title can't be empty")
        .isLength({ min: 3 })
        .withMessage('Title must be at least 3 characters'),

    body('text')
        .notEmpty()
        .withMessage("Text can't be empty")
        .isLength({ min: 10 })
        .withMessage('Text must be at least 10 characters'),

    body('tags')
        .optional()
        .isString()
        .withMessage('Tags must be a string')
        .isLength({ min: 2 })
        .withMessage('Tags must contain at least 2 characters'),

    body('imageUrl')
        .optional()
        .isURL()
        .withMessage('Image URL must be a valid URL')
];