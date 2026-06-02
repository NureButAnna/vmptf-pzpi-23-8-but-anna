import CommentModel from '../models/Comment.js';
import PostModel from '../models/Post.js';
 
export const getAll = async (req, res) => {
    try {
        const postId = req.params.postId;
 
        const comments = await CommentModel
            .find({ post: postId })
            .populate('user', 'name surname')
            .sort({ createdAt: -1 })
            .exec();
 
        res.json(comments);
    } catch (err) {
        console.log(err);
        res.status(500).json({
            message: 'Не вдалося отримати коментарі',
        });
    }
};

export const getOne = async (req, res) => {
    try {
        const { commentId } = req.params;

        const comment = await CommentModel
            .findById(commentId)
            .populate('user', 'name surname')
            .exec();

        if (!comment) {
            return res.status(404).json({
                message: 'Коментар не знайдено',
            });
        }

        res.json(comment);
    } catch (err) {
        console.log(err);
        res.status(500).json({
            message: 'Не вдалося отримати коментар',
        });
    }
};
 
export const create = async (req, res) => {
    try {
        const postId = req.params.postId;
 
        const post = await PostModel.findById(postId);
        if (!post) {
            return res.status(404).json({
                message: 'Пост не знайдено',
            });
        }
 
        const doc = new CommentModel({
            text: req.body.text,
            post: postId,
            user: req.userId,
        });
 
        const comment = await doc.save();
 
        const populated = await comment.populate('user', 'name surname');
 
        res.json(populated);
    } catch (err) {
        console.log(err);
        res.status(500).json({
            message: 'Не вдалося створити коментар',
        });
    }
};
 
export const remove = async (req, res) => {
    try {
        const { commentId } = req.params;
 
        const doc = await CommentModel.findById(commentId);
 
        if (!doc) {
            return res.status(404).json({
                message: 'Коментар не знайдено',
            });
        }
 
        if (doc.user.toString() !== req.userId) {
            return res.status(403).json({
                message: 'Немає прав для видалення',
            });
        }
 
        await CommentModel.findByIdAndDelete(commentId);
 
        res.json({ success: true });
    } catch (err) {
        console.log(err);
        res.status(500).json({
            message: 'Не вдалося видалити коментар',
        });
    }
};