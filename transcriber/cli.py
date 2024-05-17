import click
from .transcribe import transcribe_file

@click.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('-o', '--output', type=click.Path(), default=None, help='Output file for the transcription. If not specified, print to stdout.')
@click.option('--start', type=float, default=0, help='Start time in minutes (default: 0).')
@click.option('--end', type=float, default=None, help='End time in minutes (default: till end of file).')
def main(file, output, start, end):
    """Transcribe audio or video files using Whisper."""
    
    transcription = transcribe_file(file, start, end)

    if output:
        with open(output, "w") as f:
            f.write(transcription)
        click.echo(f"Transcription saved to {output}")
    else:
        click.echo(transcription)

if __name__ == "__main__":
    main()
