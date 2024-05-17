from setuptools import setup, find_packages

setup(
    name='transcriber',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
        'whisper',
        'torch',
        'pydub',
        'moviepy',
    ],
    entry_points={
        'console_scripts': [
            'transcriber = transcriber.cli:main',
        ],
    },
    python_requires='>=3.7',
    include_package_data=True,
    description='A tool for transcribing audio and video files using Whisper',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/transcriber',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
)
